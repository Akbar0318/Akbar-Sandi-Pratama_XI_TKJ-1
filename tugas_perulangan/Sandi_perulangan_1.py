# nama: Akbar Sandi Pratama
# kelas: 11 TKJ 1
# nomor absen: 3
# soal: Seorang petani memiliki 100 ekor ayam di peternakannya.

jumlah_ayam_bulan_ini = 100
target_ayam = 200
bulan = 0

while jumlah_ayam_bulan_ini < target_ayam:
    jumlah_ayam_bulan_ini += 0.05 * jumlah_ayam_bulan_ini
    bulan += 1

print("Dibutuhkan", bulan, "bulan untuk mencapai atau melebihi", target_ayam, "ekor ayam.")