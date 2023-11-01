# nama: Akbar Sandi Pratama
# kelas: 11 TKJ 1
# nomor absen: 3
# soal: Seorang petani memiliki 100 ekor ayam di peternakannya.

jarak_minggu_ini = 5
target_jarak = 10
minggu = 0

while jarak_minggu_ini < target_jarak:
    jarak_minggu_ini += 0.1 * jarak_minggu_ini
    minggu += 1

print("Dibutuhkan", minggu, "minggu untuk mencapai atau melebihi", target_jarak, "kilometer.")