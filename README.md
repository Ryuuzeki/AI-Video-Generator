# AI Full Body Video Generator (MimicMotion)

Repositori ini berisi cetak biru dan kode untuk membangun **AI Full Body Video Generator** menggunakan MimicMotion. Kamu bisa menjalankannya di Google Colab atau di mesin lokal dengan GPU NVIDIA.

## ⚠️ PENTING: Akses Model (Hugging Face)

Model utama yang digunakan (**Stable Video Diffusion**) bersifat "Gated". Artinya, kamu harus meminta akses secara manual sebelum bisa mendownloadnya:

1.  Buka link ini: [stabilityai/stable-video-diffusion-img2vid-xt-1-1](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt-1-1).
2.  Login ke akun Hugging Face kamu.
3.  Klik tombol **"Agree and access repository"** di bagian atas halaman tersebut.
4.  Buat **Access Token** di [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) (pilih tipe `Read`). Simpan token ini untuk dimasukkan ke Google Colab nanti.

## Penjelasan Parameter Utama

Agar hasil video maksimal, berikut adalah fungsi dari beberapa tombol pengaturan yang ada di aplikasi:

*   **Resolution**: Menentukan kualitas ketajaman gambar. Standar adalah **576**. Jika kamu punya GPU yang sangat kuat (seperti A100), kamu bisa menaikkannya ke 720 atau 1024.
*   **Sample Stride**: Menentukan berapa banyak frame yang dilompati.
    *   **Nilai 1 atau 2**: Hasil paling halus, tapi lambat.
    *   **Nilai 4 ke atas**: Proses sangat cepat, tapi gerakan mungkin terlihat patah-patah.
    *   *Gunakan nilai tinggi jika video referensi kamu punya FPS tinggi (misal 60 FPS).*
*   **Inference Steps**: Jumlah langkah AI untuk "menghaluskan" gambar.
    *   **20-25**: Sudah cukup bagus dan cepat.
    *   **50**: Hasil lebih detail tapi proses 2x lebih lama.
*   **Seed**: Kode angka untuk mengunci variasi acak. Gunakan angka yang sama jika ingin mengulang hasil yang identik.

## Tips Menghasilkan Kualitas Tinggi (HD)

Agar hasil video tetap tajam dan tidak kehilangan detail dari foto asli (**Simpelnya: Gambar bergeraknya mirip aslinya**):

1.  **Noise Aug Strength = 0**: Ini adalah kunci utama. Pastikan nilai ini tetap **0**. Semakin besar nilainya, AI akan semakin banyak "mengubah" detail foto asli kamu.
2.  **Foto Sumber Berkualitas Tinggi**: Gunakan foto portrait (9:16) yang sangat tajam. Hindari foto yang diambil di tempat gelap atau pecah-pecah.
3.  **Naikkan Resolution**: Standar adalah 576. Jika ingin lebih tajam, naikkan ke **720** (disarankan hanya jika menggunakan GPU T4 ke atas).
4.  **Tambah Inference Steps**: Naikkan ke **50** atau **100**. AI akan bekerja lebih keras untuk menjaga detail tekstur baju dan kulit.
5.  **Gunakan AI Face Enhancer**: Karena video AI seringkali membuat wajah sedikit blur, sangat disarankan menggunakan aplikasi seperti **Remini** atau **CodeFormer** pada hasil video akhirnya untuk mengembalikan ketajaman mata dan kulit.

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
5. **Jalankan Sel 2 (Login Hugging Face)**:
   - Masukkan Access Token yang sudah kamu buat tadi. Ini diperlukan untuk mendownload model SVD yang terkunci.
6. **Jalankan Sel 3 (Instalasi Dependensi)**:
   - Klik tombol play. Proses ini memakan waktu sekitar 2-3 menit untuk menginstal pustaka yang dibutuhkan (PyTorch, Diffusers, dll).
7. **Jalankan Sel 4 (Kloning Repositori)**:
   - Klik tombol play untuk mengunduh kode sumber MimicMotion dari GitHub. Sel ini juga secara otomatis memperbaiki bug kompatibilitas dengan PyTorch terbaru.
8. **Jalankan Sel 5 (Download Model Weights)**:
   - Klik tombol play. Ini akan mengunduh model "otak" AI (sekitar 4-5 GB). Pastikan koneksi internet stabil.
9. **Jalankan Sel 6 (Jalankan Aplikasi)**:
   - Klik tombol play. Tunggu hingga muncul pesan `Running on public URL: https://xxxx.gradio.live`.
10. **Buka Antarmuka Gradio**:
   - Klik link `.gradio.live` yang muncul.
11. **Proses Video**:
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
