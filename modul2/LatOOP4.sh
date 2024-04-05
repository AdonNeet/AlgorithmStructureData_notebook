#!/bin/bash

# Menampilkan pesan penggunaan
echo "Memulai skrip isi shell interaktif Python..."
echo " "

python << END
# Masukkan skrip dibawah ini
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

print(">>>")

print(">>> m1.ambilNama()")
print(m1.ambilNama())
print(">>> m2.ambilNIM()")
print(m2.ambilNIM())
print(">>> m3.ucapkanSalam()")
m3.ucapkanSalam()
print(">>> m3.keadaan")
print(m3.keadaan)
print(">>> m3.makan('gado-gado')")
m3.makan('gado-gado')
print(">>> m3.keadaan")
print(m3.keadaan)
print(">>> print(m3)")
print(m3)

END

echo " "
echo "Keluar dari shell interaktif Python."

