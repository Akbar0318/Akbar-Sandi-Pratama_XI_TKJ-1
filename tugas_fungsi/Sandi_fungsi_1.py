# nama: Akbar Sandi Pratama
# kelas: 11 TKJ 1
# nomor absen: 3
# soal: membuat sebuah fungsi menghitung deretan angka ganjil

def total_deret_ganjil(batas):
    total = 0
    for n in range(1, batas + 1):
        bilangan_ganjil = 2 * n - 1
        total += bilangan_ganjil
    return total

batas = int(input("Masukkan batas deret ganjil: "))
hasil = total_deret_ganjil(batas)
print("Total deret bilangan ganjil hingga batas", batas, "adalah", hasil)