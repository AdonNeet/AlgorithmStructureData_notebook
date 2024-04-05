#!/bin/bash

# Menampilkan pesan penggunaan
echo "Memulai skrip isi shell interaktif Python..."
echo " "

# Memulai shell interaktif Python
python << END
# Masukkan skrip dibawah ini
print(">>> from LatOOP3 import *")
from LatOOP3 import *

print(">>> p2 = Manusia('Budi')")
p2 = Manusia('Budi')
print(">>> p2.ucakpanSalam()")
p2.ucapkanSalam()

print(">>> ")

print(">>> ak = Manusia('Abdul Karim')")
ak = Manusia('Abdul Karim')
print(">>> ak.ucapkanSalam()")
ak.ucapkanSalam()
print(">>> ak.keadaan")
print(ak.keadaan)
print(">>> ak.makan('nasi goreng')")
ak.makan('nasi goreng')
print(">>> ak.keadaan")
print(ak.keadaan)
print(">>> ak.olahraga('renang')")
ak.olahraga('renang')
print(">>> ak.keadaan")
print(ak.keadaan)
print(">>> ak.makan('bakso')")
ak.makan('bakso')
print(">>> ak.keadaan")
print(ak.keadaan)
print(">>> ak.mengalikanDenganDua(8)")
print(ak.mengalikanDenganDua(8))


print("Keluar dari shell interaktif Python.")
END
