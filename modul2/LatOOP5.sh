#!/bin/bash

# Menampilkan pesan penggunaan
echo "Memulai skrip isi shell interaktif Python..."
echo " "

# Memulai shell interaktif Python
python << END
# Masukkan skrip dibawah ini
print(">>> from LatOOP5 import *")
from LatOOP5 import *

print(">>> m4 = MhsTIF('Badu',334,'Sragen',230000)")
m4 = MhsTIF('Badu',334,'Sragen',230000)
print(">>> m4.katakanPy()")
m4.katakanPy()
print(">>> print(m4)")
print(m4)
print(">>> m4.keadaan")
print(m4.keadaan)
print(">>> m4.makan('pecel')")
m4.makan('pecel')
print(">>> m4.keadaan")
print(m4.keadaan)
print(">>> m4.ucapkanSalam()")
m4.ucapkanSalam()

print("Keluar dari shell interaktif Python.")
END
