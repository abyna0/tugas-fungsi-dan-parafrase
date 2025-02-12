def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

print("Menghitung Faktorial")
angka = int(input("Masukkan angka untuk menghitung faktorial: "))

if angka < 0:
    print("Faktorial tidak didefinisikan untuk angka negatif")
else:
    hasil = faktorial(angka)
    print(f"Faktorial dari {angka} adalah {hasil}")
