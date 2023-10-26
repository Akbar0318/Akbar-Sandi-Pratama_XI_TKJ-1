# nama: Akbar Sandi Pratama
# kelas: XI TKJ 1
# nomor absen: 3
# soal: Sebagai seorang sistem administrator, Anda bertanggung jawab untuk memeriksa apakah suatu file di server sudah ada atau belum menggatinya.
nama_file = "data.txt"
daftar_file_di_server = ["file1.txt", "file2.txt", "data.txt", "file3.txt"]

if nama_file in daftar_file_di_server:
    print("File sudah ada")
else:
    print("File belum ada")