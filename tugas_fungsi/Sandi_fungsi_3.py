# nama: Akbar Sandi Pratama
# kelas: 11 TKJ 1
# nomor absen: 3
# soal: membuat fungsi menghitung nilai pangkat dari suatu bilangan tertentu

def hitung_pangkat(bilangan, eksponen):
    hasil = 1
    for _ in range(eksponen):
        hasil *= bilangan
    return hasil

bilangan = float(input("Masukkan bilangan: "))
eksponen = int(input("Maksukkan eksponen: "))
hasil_pangkat = hitung_pangkat(bilangan, eksponen)
print(f"{bilangan}^{eksponen} = {hasil_pangkat}")