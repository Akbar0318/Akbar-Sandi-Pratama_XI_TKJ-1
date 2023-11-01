# nama: Akbar Sandi Pratama
# kelas: 11 TKJ 1
# nomor absen: 3
# soal: Seorang pedagang memiliki 100 buah apel.

jumlah_apel_awal = 100
sisa_apel = jumlah_apel_awal
batas_sisa_apel = 20
hari = 0

while sisa_apel > batas_sisa_apel:
    sisa_apel -= 0.10 * sisa_apel
    hari += 1

print("Dibutuhkan", hari, "hari untuk sisa apel kurang dari", batas_sisa_apel, "buah.")