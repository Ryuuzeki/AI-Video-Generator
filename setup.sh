#!/bin/bash

# Exit on error
set -e

echo "--- Starting Setup ---"

# 1. Update pip, setuptools, wheel
echo "Updating build tools..."
pip install -U pip setuptools wheel

# 2. Clone MimicMotion repository if it doesn't exist
if [ ! -d "MimicMotion" ]; then
    echo "Cloning MimicMotion repository..."
    git clone https://github.com/Tencent/MimicMotion.git
else
    echo "MimicMotion repository already exists."
fi

# 3. Create models directory
echo "Creating models directory..."
mkdir -p MimicMotion/models/DWPose

# 4. Download Model Weights
echo "Downloading model weights (this may take a while)..."

# DWPose weights
if [ ! -f "MimicMotion/models/DWPose/yolox_l.onnx" ]; then
    wget https://huggingface.co/yzd-v/DWPose/resolve/main/yolox_l.onnx -O MimicMotion/models/DWPose/yolox_l.onnx
fi

if [ ! -f "MimicMotion/models/DWPose/dw-ll_ucoco_384.onnx" ]; then
    wget https://huggingface.co/yzd-v/DWPose/resolve/main/dw-ll_ucoco_384.onnx -O MimicMotion/models/DWPose/dw-ll_ucoco_384.onnx
fi

# MimicMotion weight
if [ ! -f "MimicMotion/models/MimicMotion_1-1.pth" ]; then
    wget https://huggingface.co/tencent/MimicMotion/resolve/main/MimicMotion_1-1.pth -O MimicMotion/models/MimicMotion_1-1.pth
fi

echo "--- Setup Complete! ---"
echo "PENTING: Model SVD bersifat GATED. Pastikan kamu sudah 'Accept' akses di Hugging Face"
echo "dan jalankan 'huggingface-cli login' sebelum menjalankan aplikasi."
echo ""
echo "You can now install dependencies with: pip install -r requirements.txt"
echo "And run the app with: python app.py"
