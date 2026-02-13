# AI Full Body Video Generator (MimicMotion)

Repositori ini berisi cetak biru dan kode untuk membangun **AI Full Body Video Generator** menggunakan MimicMotion. Kamu bisa menjalankannya di Google Colab atau di mesin lokal dengan GPU NVIDIA.

## Fitur
- **Pose Transfer**: Mengikuti gerakan dari video referensi.
- **Temporal Consistency**: Menjaga kualitas video tetap stabil.
- **High Resolution**: Mendukung output hingga 576p (atau lebih tinggi tergantung GPU).
- **Privacy-First**: Berjalan di environment lokal atau cloud sementara.

## Quick Start (Local/Server)

Ikuti langkah-langkah berikut untuk menjalankan di mesin lokal Anda:

1. **Clone repositori ini:**
   ```bash
   git clone <URL_REPOSI_INI>
   cd <NAMA_REPOSI>
   ```

2. **Jalankan script setup:**
   Script ini akan mengkloning repo MimicMotion asli dan mengunduh bobot model (weights) yang diperlukan secara otomatis.
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

3. **Instal dependensi:**
   Disarankan menggunakan environment virtual (seperti conda atau venv).
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan aplikasi:**
   ```bash
   python app.py
   ```
   Buka link Gradio yang muncul di terminal untuk menggunakan antarmuka web.

## Penggunaan di Google Colab

Jika Anda ingin menggunakan Google Colab:
1. Upload file `AI_Full_Body_Video_Generator.ipynb` ke Google Colab.
2. Pastikan runtime diset ke **T4 GPU** atau lebih tinggi.
3. Jalankan sel satu per satu sesuai instruksi di dalam notebook.

## Persyaratan Sistem
- **GPU NVIDIA**: Minimal 16GB VRAM direkomendasikan untuk performa optimal (seperti T4, RTX 3090/4090).
- **Python**: 3.9 atau lebih baru.
- **FFmpeg**: Terpasang di sistem.

---
*Dibuat oleh Jules (AI Assistant)*
