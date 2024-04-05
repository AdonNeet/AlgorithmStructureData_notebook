#!/bin/bash

# Menampilkan pesan penggunaan
echo "Memulai skrip isi shell interaktif Python..."
echo " "


# Memulai shell interaktif Python
python << END
# Masukkan skrip dibawah ini
print(">>> from pesan import *")
from pesan import *

print(">>> p9 = Pesan('indonesia adalah negeri yang indah')")
p9 = Pesan('Indonesia adalah negeri yang indah')
print(">>> p9.apakahTerkandung('ind')")
print(p9.apakahTerkandung('ind'))
print(">>> p9.apakahTerkandung('eka')")
print(p9.apakahTerkandung('eka'))

print(">>> \n>>> ")

print(">>> p10 = Pesan('SurakArta')")
p10 = Pesan('SurakArta')
print(">>> p10.hitungKonsonan()")
print(p10.hitungKonsonan())

print(">>> ")

print(">>> p10.hitungVokal()")
print(p10.hitungVokal())

print("Keluar dari shell interaktif Python.")
END
