import os
import sys
import math
import torch
import numpy as np
import gradio as gr
from pathlib import Path
from datetime import datetime
from PIL import Image

# Add MimicMotion to sys.path
mimic_path = os.path.join(os.getcwd(), "MimicMotion")
if os.path.exists(mimic_path):
    sys.path.append(mimic_path)
    os.chdir(mimic_path) # Change directory to MimicMotion to ensure relative paths in its code work
else:
    print("Error: MimicMotion directory not found. Please run ./setup.sh first.")
    sys.exit(1)

from omegaconf import OmegaConf
from torchvision.datasets.folder import pil_loader
from torchvision.transforms.functional import pil_to_tensor, resize, center_crop, to_pil_image

# MimicMotion imports
from mimicmotion.utils.geglu_patch import patch_geglu_inplace
patch_geglu_inplace()

from constants import ASPECT_RATIO
from mimicmotion.pipelines.pipeline_mimicmotion import MimicMotionPipeline
from mimicmotion.utils.loader import create_pipeline
from mimicmotion.utils.utils import save_to_mp4
from mimicmotion.dwpose.preprocess import get_video_pose, get_image_pose

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def preprocess(video_path, image_path, resolution=576, sample_stride=2):
    image_pixels = pil_loader(image_path)
    image_pixels = pil_to_tensor(image_pixels) # (c, h, w)
    h, w = image_pixels.shape[-2:]
    if h > w:
        w_target, h_target = resolution, int(resolution / ASPECT_RATIO // 64) * 64
    else:
        w_target, h_target = int(resolution / ASPECT_RATIO // 64) * 64, resolution
    h_w_ratio = float(h) / float(w)
    if h_w_ratio < h_target / w_target:
        h_resize, w_resize = h_target, math.ceil(h_target / h_w_ratio)
    else:
        h_resize, w_resize = math.ceil(w_target * h_w_ratio), w_target
    image_pixels = resize(image_pixels, [h_resize, w_resize], antialias=None)
    image_pixels = center_crop(image_pixels, [h_target, w_target])
    image_pixels = image_pixels.permute((1, 2, 0)).numpy()

    image_pose = get_image_pose(image_pixels)
    video_pose = get_video_pose(video_path, image_pixels, sample_stride=sample_stride)
    pose_pixels = np.concatenate([np.expand_dims(image_pose, 0), video_pose])
    image_pixels = np.transpose(np.expand_dims(image_pixels, 0), (0, 3, 1, 2))
    return torch.from_numpy(pose_pixels.copy()) / 127.5 - 1, torch.from_numpy(image_pixels) / 127.5 - 1

def run_pipeline(pipeline, image_pixels, pose_pixels, device, task_config):
    # image_pixels is already on CPU as float32 from preprocess
    image_pixels = [to_pil_image(img.to(torch.uint8)) for img in (image_pixels + 1.0) * 127.5]
    generator = torch.Generator(device=device)
    generator.manual_seed(task_config.seed)

    # Ensure pose_pixels is on the correct device and dtype (float16 for GPU)
    pose_pixels = pose_pixels.to(device, dtype=torch.float16 if device.type == "cuda" else torch.float32)

    frames = pipeline(
        image_pixels, image_pose=pose_pixels, num_frames=pose_pixels.size(0),
        tile_size=task_config.num_frames, tile_overlap=task_config.frames_overlap,
        height=pose_pixels.shape[-2], width=pose_pixels.shape[-1], fps=7,
        noise_aug_strength=task_config.noise_aug_strength, num_inference_steps=task_config.num_inference_steps,
        generator=generator, min_guidance_scale=task_config.guidance_scale,
        max_guidance_scale=task_config.guidance_scale, decode_chunk_size=8, output_type="pt", device=device
    ).frames.cpu()
    video_frames = (frames * 255.0).to(torch.uint8)
    return video_frames[0, 1:]

pipeline = None

def load_model():
    global pipeline
    if pipeline is None:
        infer_config = OmegaConf.load("configs/test.yaml")
        pipeline = create_pipeline(infer_config, device)
        if device.type == "cuda":
            pipeline.to(device, dtype=torch.float16)
    return pipeline

def generate_video(ref_image, ref_video, resolution, sample_stride, num_inference_steps, seed):
    global pipeline
    if pipeline is None:
        pipeline = load_model()

    ref_image_path = "temp_image.png"
    ref_image.save(ref_image_path)
    ref_video_path = ref_video

    task_config = OmegaConf.create({
        "ref_video_path": ref_video_path,
        "ref_image_path": ref_image_path,
        "resolution": resolution,
        "sample_stride": sample_stride,
        "num_frames": 72,
        "frames_overlap": 6,
        "noise_aug_strength": 0.02,
        "guidance_scale": 2.0,
        "num_inference_steps": num_inference_steps,
        "seed": seed,
        "fps": 15
    })

    pose_pixels, image_pixels = preprocess(
        task_config.ref_video_path, task_config.ref_image_path,
        resolution=task_config.resolution, sample_stride=task_config.sample_stride
    )

    _video_frames = run_pipeline(pipeline, image_pixels, pose_pixels, device, task_config)

    output_dir = os.path.join(mimic_path, "outputs")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"output_{datetime.now().strftime('%Y%m%d%H%M%S')}.mp4")

    save_to_mp4(_video_frames, output_path, fps=task_config.fps)

    return output_path

def main():
    with gr.Blocks() as demo:
        gr.Markdown("# MimicMotion AI Full Body Video Generator")
        gr.Markdown("Pastikan Anda telah menjalankan `./setup.sh` sebelum menjalankan aplikasi ini.")
        with gr.Row():
            with gr.Column():
                ref_image = gr.Image(label="Reference Image (Full Body)", type="pil")
                ref_video = gr.Video(label="Reference Video (Motion)")
                resolution = gr.Slider(minimum=256, maximum=1024, value=576, step=64, label="Resolution")
                sample_stride = gr.Slider(minimum=1, maximum=10, value=2, step=1, label="Sample Stride")
                num_inference_steps = gr.Slider(minimum=1, maximum=50, value=25, step=1, label="Inference Steps")
                seed = gr.Number(value=42, label="Seed")
                btn = gr.Button("Generate")
            with gr.Column():
                output_video = gr.Video(label="Generated Video")

        btn.click(
            generate_video,
            inputs=[ref_image, ref_video, resolution, sample_stride, num_inference_steps, seed],
            outputs=output_video
        )

    demo.launch(share=True)

if __name__ == "__main__":
    main()
