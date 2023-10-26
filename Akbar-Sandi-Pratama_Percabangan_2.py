# nama: Akbar Sandi Pratama
# kelas: XI TKJ 1
# nomor absen: 3
# soal: Sebagai seorang manajer proyek, Anda harus menentukan apakah suatu proyek akan selesai tepat waktu atau terlambat.
from datetime import datetime

estimasi_selesai = input("Masukkan estimasi waktu selesai proyek (YYYY-MM-DD): ")
estimasi_selesai = datetime.strptime(estimasi_selesai, '%Y-%m-%d')

tanggal_target = input("Masukkan tanggal target selesai (YYYY-MM-DD): ")
tanggal_target = datetime.strptime(tanggal_target, '%Y-%m-%d')

if estimasi_selesai <= tanggal_target:
    print("Tepat waktu")
else:
    print("Terlambat")