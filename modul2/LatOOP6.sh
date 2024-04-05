#!/bin/bash

# Menampilkan pesan penggunaan
echo "Memulai skrip isi shell interaktif Python..."
echo " "

# Memulai shell interaktif Python
python << END
print(">>> from LatOOP4 import *")
from LatOOP4 import *

print(
">>> m1 = Mahasiswa('Jamil',234,'Surakarta',250000)\n" + 
">>> m2 = Mahasiswa('Andi',365,'Magelang',275000) \n" +
">>> m3 = Mahasiswa('Sri', 676,'Yogyakarta',240000)"
)

m1 = Mahasiswa('Jamil',234,'Surakarta',250000)
m2 = Mahasiswa('Andi',365,'Magelang',275000)
m3 = Mahasiswa('Sri', 676,'Yogyakarta',240000)

daftar = [m1, m2, m3]

print(">>> for i in daftar: print(i.NIM)\n")
for i in daftar: print(i.NIM) 

print(">>> for i in daftar: print(i)\n")
for i in daftar: print(i)

END

echo " "
echo "Keluar dari shell interaktif Python."


