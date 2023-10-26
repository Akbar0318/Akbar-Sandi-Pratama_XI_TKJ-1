# nama: Akbar Sandi Pratama
# kelas: XI TKJ 1
# nomor absen: 3
# soal: Di sebuah toko online, anda bertanggung jawab untuk menghitung diskon berdasarkan total belanjaan pelanggan.
total_belanjaan = float(input("Total belanjaan anda: "))

if total_belanjaan > 500000:
    diskon = total_belanjaan * 0.10
elif total_belanjaan >= 300000:
    diskon = total_belanjaan * 0.05
else:
    diskon = 0

total_pembayaran = total_belanjaan - diskon
print(f"Total pembayaran setelah diskon: {total_pembayaran}")