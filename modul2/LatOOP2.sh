#!/bin/bash

# Menampilkan pesan penggunaan
echo "Memulai skrip isi shell interaktif Python..."
echo " "

# Memulai shell interaktif Python
python << END
print(">>> from LatOOP2 import *")
from LatOOP2 import *

print(
">>> pesanA = Pesan('Aku suka kuliah ini')\n" +
">>> pesanB = Pesan('Surakarta: the Spirit of Java')"
)

pesanA = Pesan('Aku suka kuliah ini')
pesanB = Pesan('Surakarta: the Spirit of Java')

print(">>>")
print(">>> pesanA.cetakIni()")
pesanA.cetakIni()
print(">>> pesanA.cetakJumlahKarakterku()")
pesanA.cetakJumlahKarakterku()
print(">>> pesanB.cetakJumlahKarakterku()")
pesanB.cetakJumlahKarakterku()
print(">>> pesanA.cetakPakaiHurufKapital()")
pesanA.cetakPakaiHurufKapital()
print(">>> pesanA.cetakPakaiHurufKecil()")
pesanA.cetakPakaiHurufKecil()
print(">>> pesanA.perbarui('Aku senang struktur data')")
pesanA.perbarui('Aku senang struktur data')
print(">>> pesanA.cetakIni()")
pesanA.cetakIni()

print("Keluar dari shell interaktif Python.")
END
