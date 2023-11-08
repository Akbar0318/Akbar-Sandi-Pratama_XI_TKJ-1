# nama: Akbar Sandi Pratama
# kelas: 11 TKJ 1
# nomor absen: 3
# soal: menghitung sebuah faktorial

def faktorial(n):
    if n == 0:
        return 1
    else:
        hasil = 1
        for i in range(1, n + 1):
            hasil *= i
        return hasil

bilangan = int(input("Masukkan bilangan: "))
hasil_faktorial = faktorial(bilangan)
print("Faktorial dari", bilangan, "adalah", hasil_faktorial)