#!/bin/bash

# Menampilkan pesan penggunaan
echo "Memulai skrip isi shell interaktif Python..."
echo " "


# Memulai shell interaktif Python
python << END
# Masukkan skrip dibawah ini
print(">>> from dataMhs import *")
from dataMhs import *

print(
">>> m1 = Mahasiswa('Jamil',234,'Surakarta',250000)\n" +
">>> m2 = Mahasiswa('Andi',365,'Magelang',275000) \n" +
">>> m3 = Mahasiswa('Sri', 676,'Yogyakarta',240000)"
)

m1 = Mahasiswa('Jamil',234,'Surakarta',250000)
m2 = Mahasiswa('Andi',365,'Magelang',275000)
m3 = Mahasiswa('Sri', 676,'Yogyakarta',240000)

print(">>> ")

print(">>> m1.ambilKotaTinggal()")
print(m1.ambilKotaTinggal())

print(">>> ")

print(">>> m2.perbaruiKotaTinggal('Sleman')")
m2.perbaruiKotaTinggal('Sleman')
print(">>> m2.ambilKotaTinggal()") 
print(m2.ambilKotaTinggal())

print(">>> ")

print(">>> m3.ambilUangSaku()")
print(m3.ambilUangSaku())
print(">>> m3.tambahUangSaku(50000)")
m3.tambahUangSaku(50000)
print(">>> m3.ambilUangSaku()")
print(m3.ambilUangSaku())


print("Keluar dari shell interaktif Python.")
END
