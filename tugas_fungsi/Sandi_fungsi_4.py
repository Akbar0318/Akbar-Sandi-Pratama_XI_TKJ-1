# nama: Akbar Sandi Pratama
# kelas: 11 TKJ 1
# nomor absen: 3
# soal: 

def hitung_jumlah_digit(bilangan):
    bilangan_str = str(bilangan)
    total = 0
    for digit in bilangan_str:
        total += int(digit)
    return total

bilangan = int(input("Masukkan bilangan: "))
hasil = hitung_jumlah_digit(bilangan)
print("Jumlah digit dari", bilangan, "adalah", hasil)