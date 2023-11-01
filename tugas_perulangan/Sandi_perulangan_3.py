# nama: Akbar Sandi Pratama
# kelas: 11 TKJ 1
# nomor absen: 3
# soal: Sebuah investasi awal sebesar 10.000 dollar tumbuh sebesar 6% setiap tahunnya.

nilai_investasi_awal = 10000
target_nilai_investasi = 20000
tahun = 0

while nilai_investasi_awal < target_nilai_investasi:
    nilai_investasi_awal += 0.06 * nilai_investasi_awal
    tahun += 1

print("Dibutuhkan", tahun, "tahun untuk mencapai atau melebihi nilai investasi sebesar", target_nilai_investasi, "dollar.")