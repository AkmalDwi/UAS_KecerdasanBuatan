Nama : Akmal Dwi Syahputra

NIM : 211011401524

Kelas : 06TPLP021

UAS Kecerdasan Buatan

Referensi : https://www.youtube.com/watch?v=rfHq9HVdRqw

Aplikasi Detector dan Translator Languages adalah antarmuka pengguna grafis (GUI) yang dibangun dengan Tkinter yang menyediakan fungsionalitas untuk mendeteksi bahasa, menerjemahkan teks antara berbagai bahasa, mengonversi ucapan ke teks, dan mengonversi teks ke ucapan. 

Fitur
Deteksi Bahasa: Mendeteksi bahasa teks input secara otomatis.

Terjemahan Teks: Menerjemahkan teks dari satu bahasa ke bahasa lain.

Hapus Teks: Menghapus bidang teks input dan teks terjemahan.

Ucapan ke Teks: Mengonversi kata yang diucapkan menjadi teks.

Teks ke Ucapan: Mengonversi teks menjadi kata yang diucapkan.

tkinter: Paket GUI standar Python.

googletrans==4.0.0-rc1: Pustaka python gratis dan tak terbatas yang mengimplementasikan API Google Translate.

textblob: Pustaka sederhana untuk memproses data tekstual.

langid: Alat identifikasi bahasa.

speech_recognition: Pustaka untuk melakukan pengenalan ucapan.

pyttsx3: Pustaka konversi teks ke ucapan dalam Python.

Menginstal pustaka yang dibutuhkan menggunakan pip:

pip install googletrans==4.0.0-rc1 textblob langid SpeechRecognition pyttsx3

Antarmuka Pengguna

Input Teks: Terdapat dua kotak teks. Kotak teks di sebelah kiri adalah untuk input teks asli, dan kotak teks di sebelah kanan menampilkan teks yang telah diterjemahkan.

Pemilihan Bahasa: Dua combobox tersedia untuk memilih bahasa sumber dan bahasa target.

Tombol:

Translate: Menerjemahkan teks dari bahasa sumber ke bahasa target.

Clear: Menghapus kedua kotak teks.

Detect Language: Mendeteksi bahasa teks di kotak teks asli.

Speech to Text: Mengonversi kata yang diucapkan menjadi teks dan menampilkannya di kotak teks asli.

Listen to Translation: Mengonversi teks terjemahan menjadi ucapan.

Fungsi

detect_language()

Menggunakan langid untuk mendeteksi bahasa teks di kotak teks asli dan menetapkan bahasa yang sesuai di combobox bahasa sumber.

translate_it()

Menerjemahkan teks dari bahasa sumber ke bahasa target menggunakan textblob.

clear()

Menghapus teks dari kedua kotak teks asli dan kotak teks terjemahan.

recognize_speech()

Mengonversi ucapan menjadi teks menggunakan speech_recognition dan menampilkannya di kotak teks asli.

speak_text()

Mengonversi teks di kotak teks terjemahan menjadi ucapan menggunakan pyttsx3.

Catatan

Pastikan memiliki koneksi internet aktif agar fitur pengenalan ucapan dan terjemahan berfungsi dengan baik.

Antarmuka aplikasi memiliki ukuran tetap dan tidak dapat diubah ukurannya.

Penanganan kesalahan diimplementasikan untuk menampilkan pesan yang sesuai jika terjadi kesalahan pada operasi apa pun.
