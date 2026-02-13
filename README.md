# AI Full Body Video Generator (MimicMotion)

Repositori ini berisi cetak biru dan kode untuk membangun **AI Full Body Video Generator** menggunakan MimicMotion. Kamu bisa menjalankannya di Google Colab atau di mesin lokal dengan GPU NVIDIA.

## Panduan Lengkap Google Colab (Langkah demi Langkah)

Ikuti langkah-langkah ini dengan teliti agar tidak ada yang terlewat:

1. **Buka Google Colab**: Kunjungi [colab.research.google.com](https://colab.research.google.com/).
2. **Upload Notebook**:
   - Klik tab **Upload**.
   - Pilih file `AI_Full_Body_Video_Generator.ipynb` dari repositori ini.
3. **Aktifkan GPU (Sangat Penting)**:
   - Klik menu **Runtime** di bagian atas.
   - Pilih **Change runtime type**.
   - Pada bagian **Hardware accelerator**, pilih **T4 GPU**.
   - Klik **Save**.
4. **Jalankan Sel 1 (Cek GPU)**:
   - Klik tombol play pada sel pertama. Pastikan muncul tabel informasi GPU (misalnya Tesla T4).
5. **Jalankan Sel 2 (Instalasi Dependensi)**:
   - Klik tombol play. Proses ini memakan waktu sekitar 2-3 menit untuk menginstal pustaka yang dibutuhkan (PyTorch, Diffusers, dll).
6. **Jalankan Sel 3 (Kloning Repositori)**:
   - Klik tombol play untuk mengunduh kode sumber MimicMotion dari GitHub.
7. **Jalankan Sel 4 (Download Model Weights)**:
   - Klik tombol play. Ini akan mengunduh model "otak" AI (sekitar 4-5 GB). Pastikan koneksi internet stabil.
8. **Jalankan Sel 5 (Jalankan Aplikasi)**:
   - Klik tombol play. Tunggu hingga muncul pesan `Running on public URL: https://xxxx.gradio.live`.
9. **Buka Antarmuka Gradio**:
   - Klik link `.gradio.live` yang muncul.
10. **Proses Video**:
    - **Upload Image**: Masukkan foto badan penuh (Full Body).
    - **Upload Video**: Masukkan video gerakan referensi.
    - **Klik Generate**: Tunggu proses selesai (biasanya 5-10 menit tergantung panjang video).
    - **Download**: Setelah selesai, video hasil bisa langsung diunduh.

## Quick Start (Local/Server)

1. **Clone repositori ini:**
   ```bash
   git clone <URL_REPOSI_INI>
   cd <NAMA_REPOSI>
   ```
2. **Setup:**
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```
3. **Instal & Jalankan:**
   ```bash
   pip install -r requirements.txt
   python app.py
   ```

## Persyaratan Sistem
- **GPU NVIDIA**: Minimal 16GB VRAM (T4 di Colab sudah cukup).
- **FFmpeg**: Terpasang di sistem.

---
*Dibuat oleh Jules (AI Assistant)*
