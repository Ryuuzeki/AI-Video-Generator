# AI Full Body Video Generator (MimicMotion)

Repositori ini berisi cetak biru dan kode untuk membangun **AI Full Body Video Generator** menggunakan MimicMotion di Google Colab.

## Daftar Isi
- [Fitur](#fitur)
- [Teknologi](#teknologi)
- [Cara Penggunaan](#cara-penggunaan)
- [Persyaratan Sistem](#persyaratan-sistem)

## Fitur
- **Pose Transfer**: Mengikuti gerakan dari video referensi.
- **Temporal Consistency**: Menjaga kualitas video tetap stabil.
- **High Resolution**: Mendukung output hingga 576p (atau lebih tinggi tergantung GPU).
- **Privacy-First**: Berjalan di environment sementara Cloud.

## Teknologi
- **MimicMotion**: Framework utama untuk video generation.
- **Stable Diffusion Video (SVD)**: Backbone model.
- **DWPose**: Untuk ekstraksi gerakan tubuh.
- **Gradio**: Antarmuka pengguna (UI).

## Cara Penggunaan
1. Buka [Google Colab](https://colab.research.google.com/).
2. Upload file `AI_Full_Body_Video_Generator.ipynb` ke Google Colab.
3. Pastikan runtime diset ke **T4 GPU**.
4. Jalankan sel satu per satu.
5. Setelah sel terakhir berjalan, klik link Gradio (biasanya berakhir dengan `.gradio.live`) untuk membuka UI.
6. Upload foto target dan video referensi, lalu klik **Generate**.

## Persyaratan Sistem
- Google Colab (Free tier dengan T4 GPU sudah cukup).
- Memori GPU minimal 16GB direkomendasikan untuk performa optimal (T4 memiliki 16GB).

---
*Dibuat oleh Jules (AI Assistant)*
