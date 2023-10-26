# nama: Akbar Sandi Pratama
# kelas: XI TKJ 1
# nomor absen: 3
# soal: Sebagai seorang kasir di toko, Anda harus menghitung jumlah diskon bedasarkan total belanjaan pelanggan dan jenis anggota (anggota biasa atau anggota premium).
total_belanjaan = float(input("Masukkan total belanjaan: "))
status_anggota = input("Masukkan status anggota (biasa/premium): ")

if status_anggota == "premium":
    if total_belanjaan > 500000:
        diskon = 0.15
    else:
        diskon = 0.10
elif status_anggota == "biasa":
    if total_belanjaan > 300000:
        diskon = 0.07
    else:
        diskon = 0.00
else:
    print("Status anggota tidak valid. harap masukkan 'biasa' atau 'premium'.")
    exit(1)

total_setelah_diskon = total_belanjaan - (total_belanjaan * diskon)

print(f"Total belanjaan: Rp {total_belanjaan:.2f}")
print(f"Diskon: {diskon * 100}%")
print(f"Total setelah diskon: Rp {total_setelah_diskon:.2f}")