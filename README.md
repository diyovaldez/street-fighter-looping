# 🕹️ ASCII Street Fighter II — Terminal Animation

> Animasi pertarungan **RYU vs ZANGIEF** berbasis karakter ASCII yang berjalan langsung di terminal, dibuat murni dengan Python tanpa library eksternal.

```
    ╔══════════════════════════════════╗
    ║   STREET FIGHTER II   ROUND 3   ║
    ╚══════════════════════════════════╝
    RYU  [████████████████████] ZANGIEF
    RYU  [██████████████░░░░░░] ZANGIEF

    ┌────────────────────────────────┐
    │        o>  ===(O)===  _o_      │
    │       /|>             / \      │
    │       / \                      │
    └────────────────────────────────┘
       RYU: "HADOUKEN!!!"
```

---

## 📋 Tentang Proyek

Proyek ini adalah eksperimen **ASCII art animation** di terminal — teknik menampilkan animasi dengan cara mencetak ulang karakter teks ke layar setiap beberapa milidetik, menciptakan ilusi gerakan layaknya flip-book. Terinspirasi dari era game arcade klasik tahun 1990-an, khususnya **Street Fighter II (1991)** oleh Capcom.

Tujuan proyek ini bukan untuk membuat ulang game-nya, melainkan untuk mendemonstrasikan bahwa **animasi yang menarik bisa dibuat hanya dengan karakter teks biasa** — tanpa grafis, tanpa library game, tanpa GUI.

---

## ✨ Fitur

- **23 frame animasi** yang menceritakan satu babak penuh pertarungan
- **Warna terminal ANSI** — merah untuk aksi intens, kuning untuk momen spesial
- **Progress bar real-time** menunjukkan posisi animasi (0–30 detik)
- **Loop tanpa batas** — pertarungan ulang otomatis setiap selesai, match counter terus bertambah
- **Graceful exit** — `Ctrl+C` keluar dengan bersih dan menampilkan total match yang sudah dimainkan
- **Zero dependency** — hanya butuh Python 3, tidak perlu install apapun

---

## 🚀 Cara Menjalankan

### Prasyarat
- Python 3.x (sudah terinstall di Linux/macOS, atau download di [python.org](https://python.org))
- Terminal yang mendukung warna ANSI: **Linux terminal**, **macOS Terminal/iTerm2**, **Windows Terminal**

### Jalankan

```bash
# Clone atau download file
git clone https://github.com/username/ascii-street-fighter.git
cd ascii-street-fighter

# Langsung jalankan
python street_fighter_ascii.py
```

Untuk keluar kapan saja, tekan `Ctrl+C`.

### Kompatibilitas Terminal

| Platform       | Terminal            | Status  |
|----------------|---------------------|---------|
| Linux          | Bash / Zsh          | ✅ Full |
| macOS          | Terminal / iTerm2   | ✅ Full |
| Windows        | Windows Terminal    | ✅ Full |
| Windows        | CMD (lama)          | ⚠️ Warna mungkin tidak muncul |

> **Tips Windows CMD lama:** jalankan `color` di CMD terlebih dahulu, atau gunakan Windows Terminal / PowerShell.

---

## 🗂️ Struktur File

```
ascii-street-fighter/
├── street_fighter_ascii.py   # Script utama
└── README.md                 # Dokumentasi ini
```

---

## 🔬 Penjelasan Teknis

### Bagaimana Animasi Ini Bekerja?

Animasi terminal bekerja dengan prinsip **"cetak ulang — hapus — cetak lagi"**. Setiap ~120ms, program menghapus seluruh layar dan mencetak frame berikutnya. Karena pergantian terjadi sangat cepat, mata manusia melihatnya sebagai gerakan.

```
[hapus layar] → [cetak frame 1] → [tunggu 120ms]
             → [hapus layar] → [cetak frame 2] → [tunggu 120ms]
             → ... dst
```

Ini persis cara kerja **flip-book** atau **film seluloid** — serangkaian gambar diam yang ditampilkan cepat.

### Escape Code ANSI

Warna dan kontrol terminal menggunakan **ANSI escape codes** — urutan karakter khusus yang dikenali terminal sebagai perintah, bukan teks biasa.

```python
CLEAR  = "\033[2J\033[H"   # Hapus seluruh layar + pindah cursor ke pojok kiri atas
RED    = "\033[91m"         # Aktifkan warna merah terang
YELLOW = "\033[93m"         # Aktifkan warna kuning terang
BOLD   = "\033[1m"          # Aktifkan teks tebal
RESET  = "\033[0m"          # Reset semua warna/format ke default
```

Angka `\033` adalah karakter **ESC** (ASCII 27) dalam notasi oktal. Semua perintah diawali dengan `\033[` lalu diakhiri huruf yang menentukan jenis perintahnya.

### Struktur Data FRAMES

Setiap frame disimpan sebagai **tuple** berisi dua elemen:

```python
FRAMES = [
    (WARNA, "teks_ascii_frame"),
    (WARNA, "teks_ascii_frame"),
    ...
]
```

```python
# Contoh satu frame
(YELLOW, """
    ┌────────────────────────────────┐
    │   o>  ===(O)===  _o_           │
    │  /|>             / \           │
    └────────────────────────────────┘
       RYU: "HADOUKEN!!!" """)
```

Warna disimpan bersama frame-nya agar setiap momen cerita punya nuansa visual berbeda — merah untuk ketegangan, kuning untuk momen penting.

### Logika Pemilihan Frame

```python
fi = min(int((elapsed / total) * n), n - 1)
```

Rumus ini memetakan waktu yang berjalan (0–30 detik) ke indeks frame (0–22) secara proporsional:

```
elapsed = 0s   → fi = 0   (frame pertama: FIGHT!)
elapsed = 15s  → fi = 11  (frame tengah: SHORYUKEN)
elapsed = 29s  → fi = 22  (frame akhir: RYU WINS)
```

`min(..., n-1)` memastikan indeks tidak pernah melewati batas array meskipun ada selisih kecil di timing.

### Progress Bar

```python
def draw_bar(elapsed, total=30.0, width=38):
    filled = int((elapsed / total) * width)
    bar = "█" * filled + "░" * (width - filled)
    pct = int((elapsed / total) * 100)
    return f"  [{bar}] {pct}%  {elapsed:.1f}s / {total:.0f}s"
```

Blok `█` (U+2588) mengisi bar sesuai persentase waktu berjalan, sisanya diisi `░` (U+2591) sebagai area kosong. Hasilnya terlihat seperti loading bar.

### Loop Tanpa Batas

```python
def run():
    match_num = 1
    try:
        while True:              # loop luar: terus berulang selamanya
            start = time.time()
            while True:          # loop dalam: jalankan satu pertarungan 30 detik
                elapsed = time.time() - start
                if elapsed >= 30.0:
                    break        # keluar dari loop dalam → tampil GAME OVER
                # ... render frame
            print(GAME_OVER)
            time.sleep(2.5)
            match_num += 1       # tambah counter, mulai lagi dari loop luar
    except KeyboardInterrupt:    # tangkap Ctrl+C
        sys.exit(0)              # keluar dengan bersih
```

`KeyboardInterrupt` adalah exception yang Python lemparkan secara otomatis saat user menekan `Ctrl+C`. Dengan menangkapnya di `except`, program bisa menampilkan pesan perpisahan sebelum benar-benar berhenti.

---

## 🎮 Alur Cerita Pertarungan

Ke-23 frame menceritakan satu babak lengkap dengan plot twist:

| Frame | Waktu | Kejadian |
|-------|-------|----------|
| 0 | 0s | Round 3 dimulai — kedua fighter berhadapan |
| 1–2 | ~3s | Ryu dan Zangief saling mendekat |
| 3–4 | ~5s | Ryu charging → melepas **Hadouken** |
| 5–6 | ~8s | Hadouken kena Zangief — **-200 HP** |
| 7–8 | ~10s | Zangief **RAGE** dan maju menyerang |
| 9–10 | ~13s | Zangief coba **Grab** — Ryu berhasil **dodge** |
| 11–12 | ~15s | Ryu counter dengan **SHORYUKEN** — Zangief jatuh **-500 HP** |
| 13–14 | ~18s | Zangief bangkit, aktifkan **Super Combo** |
| 15–16 | ~20s | Zangief tangkap Ryu — **Spinning Piledriver -700 HP** — Ryu DOWN |
| 17 | ~22s | *Plot twist* — Ryu bangkit: *"...not yet."* |
| 18–19 | ~24s | Ryu charge **Metsu Hadouken** (Super Art) |
| 20–21 | ~27s | Impact besar — Zangief HP = 0 — **K.O.!!!** |
| 22–23 | ~29s | **RYU WINS** — Battle Results |

---

## 💡 Konsep yang Dipelajari dari Proyek Ini

Proyek sederhana ini menyentuh beberapa konsep pemrograman yang menarik:

- **Terminal control** — bagaimana program mengontrol tampilan terminal via escape codes
- **Time-based animation** — menggunakan waktu nyata (bukan frame counter) sebagai patokan animasi, sehingga kecepatan konsisten di semua mesin
- **Data-driven design** — memisahkan konten (FRAMES) dari logika (fungsi `run`), sehingga mudah menambah frame baru tanpa mengubah logika
- **Graceful shutdown** — menangani interrupt signal agar program berhenti dengan bersih
- **ASCII art** — representasi visual menggunakan karakter teks: `o/` untuk kepala+tangan, `/|\\` untuk badan, `/ \\` untuk kaki

---

## 🛠️ Kemungkinan Pengembangan

Beberapa ide untuk mengembangkan proyek ini lebih lanjut:

- Tambah karakter lain (Ken, Chun-Li, Guile) sebagai pilihan fighter
- Tambah **sound effect** via `beep` atau library `playsound`
- Buat sistem **input keyboard** agar user bisa memilih serangan
- Export animasi ke format **GIF** menggunakan `ttyrec` atau `asciinema`
- Buat versi **multiplayer lokal** dengan dua keyboard input

---

## 📜 Lisensi

Proyek ini bebas digunakan untuk keperluan belajar dan portofolio. Street Fighter II adalah merek dagang milik **Capcom Co., Ltd.** — proyek ini bukan afiliasi resmi dan dibuat murni untuk tujuan edukasi.

---

## 👤 Author

Dibuat dengan ❤️ dan karakter `o/` oleh **[nama kamu]**

> *"The answer lies in the heart of battle!"* — Ryu
