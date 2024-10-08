# Spotify Track Search and Playback

## Deskripsi

Proyek ini adalah aplikasi Python sederhana yang memungkinkan pengguna untuk mencari lagu di Spotify dan memutar lagu tersebut melalui browser web. Menggunakan API Spotify, aplikasi ini memberikan informasi tentang lagu-lagu yang ditemukan berdasarkan query pencarian dan memungkinkan pengguna untuk memilih dan memutar lagu yang mereka inginkan.

## Fitur

- **Pencarian Lagu**: Pengguna dapat mencari lagu berdasarkan judul, artis, atau album.
- **Menampilkan Hasil**: Aplikasi menampilkan daftar hasil pencarian termasuk nama lagu, artis, album, tanggal rilis, dan popularitas.
- **Memutar Lagu**: Pengguna dapat memilih nomor dari daftar lagu untuk memutar lagu di Spotify melalui browser web.
- **Pencarian Ulang**: Setelah memutar lagu, pengguna dapat memilih untuk mencari lagu baru atau memutar lagu lainnya dari daftar.
- **Keluar**: Pengguna dapat keluar dari aplikasi dengan mengetikkan `exit`.

## Teknologi yang Digunakan

- **Python**: Bahasa pemrograman untuk logika aplikasi.
- **Spotipy**: Library Python untuk berinteraksi dengan API Spotify.
- **Webbrowser**: Modul Python untuk membuka tautan di browser web.

## Persyaratan

- Python 3.x
- Library Python: `spotipy`

## Instalasi

1. **Clone Repository**:

   ```bash
   git clone https://github.com/GhandiZero0X/SpotLyricML.git

2. **Masukkan Client ID dan Client Secret:**:
    Gantilah client_id dan client_secret di dalam kode dengan kredensial Spotify Anda. Untuk mendapatkan kredensial, kunjungi
    ```bash
    https://developer.spotify.com/dashboard

3. **Install Dependencies:**:
    ```bash
    pip install spotipy

## Cara Menggunakan
1. Jalankan skrip Python:
    ```bash
    python spotify_ml.py
2. Masukkan query pencarian (judul lagu, artis, atau album) saat diminta.
3. Pilih nomor lagu dari daftar hasil pencarian untuk memutarnya di Spotify.
4. Ketik 0 untuk kembali ke pencarian atau ketik exit untuk keluar dari aplikasi.
