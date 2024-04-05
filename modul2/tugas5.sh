#!/bin/bash

# Menampilkan pesan penggunaan
echo "Memulai skrip isi shell interaktif Python..."
echo " "


# Memulai shell interaktif Python
python << END
# Masukkan skrip dibawah ini
print(">>> from dataMhs import *")
from dataMhs import *

print(">>> m1 = Mahasiswa('Jamil',234,'Surakarta',250000)")
m1 = Mahasiswa('Jamil',234,'Surakarta',250000)
print(">>> m1.listKuliah")
print(m1.listKuliah)
print(">>> m1.ambilKuliah('Matematika Dasar')")
m1.ambilKuliah('Matematika Diskrit')
print(">>> m1.ambilKuliah('Algoritma dan Struktur Data')")
m1.ambilKuliah('Algoritma dan Struktur Data')
print(">>> m1.ambilKuliah('Matematika Diskrit')")
m1.ambilKuliah('Matematika Dasar')
print(">>> m1.listKuliah")
print(m1.listKuliah)
print(">>> m1.hapusKuliah('Matematika Dasar')")
m1.hapusKuliah('Matematika Dasar')
print(">>> m1.listKuliah")
print(m1.listKuliah)

print("Keluar dari shell interaktif Python.")
END
