#!/bin/bash

# Menampilkan pesan penggunaan
echo "Memulai skrip isi shell interaktif Python..."
echo " "


# Memulai shell interaktif Python
python << END
# Masukkan skrip dibawah ini
print(">>> from SMA import *")
from SMA import *

print(">>> A = SiswaSMA('Adon', 177013, 'MIPA', 'Kudus', 100000)")
A = SiswaSMA('Adon', 177013, 'MIPA', 'Kudus', 100000)
print(">>> print(A)")
print(A)
print(">>> A.hobi")
print(A.hobi)
print(">>> A.addHobi('bersepeda')")
A.addHobi('bersepeda')
print(">>> A.hobi")
print(A.hobi)
print(">>> A.addUangSaku(50000)")
A.addUangSaku(50000)
print(">>> A.cekUangSaku()")
print(A.cekUangSaku())
print(">>> A.addHobi('ngewibu')")
A.addHobi('ngewibu')
print(">>> A.delHobi('bersepeda')")
A.delHobi('bersepeda')
print(">>> A.hobi")
print(A.hobi)
print(">>> A.gantiTempat('Isekai')")
A.gantiTempat('Isekai')
print(">>> A.cekKotaTinggal()")
print(A.cekKotaTinggal())

print("Keluar dari shell interaktif Python.")
END
