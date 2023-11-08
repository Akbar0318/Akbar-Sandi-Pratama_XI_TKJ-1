# nama: Akbar Sandi Pratama
# kelas: 11 TKJ 1
# nomor absen: 3
# soal: 

def fibonacci(n):
    if n <= 0:
        return "Bilangan Fibonacci hanya tersedia untuk n > 0"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n -1) + fibonacci(n -2)

n = int(input("Masukkan nilai n untuk bilangan fibonacci ke-n: "))
hasil = fibonacci(n)
print(f"Bilangan Fibonacci ke-{n} adalah {hasil}")