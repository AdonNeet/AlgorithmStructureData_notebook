#!/bin/bash

# Menampilkan pesan penggunaan
echo "Memulai skrip isi shell interaktif Python..."
echo " "


# Memulai shell interaktif Python
python << END
# Masukkan skrip dibawah ini
print(">>> import ModulePythonPertamaku")
import ModulePythonPertamaku 
print(">>> ModulePythonPertamaku.ucapkanSalam()")
ModulePythonPertamaku.ucapkanSalam()
print(">>> ModulePythonPertamaku.kuadraktan(5)")
print(ModulePythonPertamaku.kuadratkan(5))
print(">>> ModulePythonPertamakku.buah")
print(ModulePythonPertamaku.buah)

print(">>> \n>>>")

print(">>> import ModulePythonPertamaku as mpp")
import ModulePythonPertamaku as mpp
print(">>> mpp.ucapkanSalam()")
mpp.ucapkanSalam()
print(">>> mpp.daftarBaju")
print(mpp.daftarBaju)
print(">>> mpp.jumlahBaju")
print(mpp.jumlahBaju)

print(">>> \n>>> ")

print(">>> from ModulePythonPertamaku import kuadratkan, daftarBaju")
from ModulePythonPertamaku import kuadratkan, daftarBaju
print(">>> kuadratkan(6)")
print(kuadratkan(6))
print(">>> daftarBaju")
print(daftarBaju)

print(">>> \n>>> ")

print(">>> from ModulePythonPertamaku import ucapkanSalam as ucap")
from ModulePythonPertamaku import ucapkanSalam as ucap
print(">>>  ucap()")
ucap()

print("Keluar dari shell interaktif Python.")
END
