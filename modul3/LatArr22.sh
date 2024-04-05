#!/bin/bash

# fungsi cetak(x) di dalam skrip Bash
prt() {
        echo "print(${1})"
}

cetak() {
        echo "print('${1}')"
}

ccetak() {      # ini untuk mencetak print didalam print
        echo "print(\">>> ${1}\")"
}

# Simpan kalimat atau perintah yang mungkin dijalankan berulang


# Menampilkan pesan penggunaan
echo "Memulai skrip isi shell interaktif Python..."
echo " "

# Memulai shell interaktif Python
python << END
$(ccetak "$(prt "[x**2 for x in range(0,7)]")")
$(prt "[x**2 for x in range(0,7)]")
$(ccetak " ")
$(ccetak "$(prt "[(x, x**2) for x in range(7)]")")
$(prt "[(x, x**2) for x in range(7)]")
$(ccetak " ")
$(ccetak "$(prt "[x**2 for x in range(15) if x%2==0]")")
$(prt "[x**2 for x in range(0,7)]")
$(ccetak " ")
$(ccetak "$(prt "[3 for i in range(5)]")")
$(prt "[x**2 for x in range(0,7)]")
$(ccetak " ")
$(ccetak "$(prt "[ [0 for j in range(3)] for i in range(3) ]")") # membuat martiks 0
$(prt "[ [0 for j in range(3)] for i in range(3) ]")
$(ccetak " ")
$(ccetak "$(prt "[ [ 1 if j==i else 0 for j in range(3) ] for i in range(3) ]")") # membuat matriks identitas
$(prt "[ [ 1 if j==i else 0 for j in range(3) ] for i in range(3) ]")
$(ccetak " ")
$(ccetak "$(prt "d = 'Yogyakarta dan Surakarta'")") # print vokal saja
d = 'Yogyakarta dan Surakarta'
$(prt "[x for x in d if x in 'aiueoAIUEO']")
$(ccetak " ")
$(ccetak "from apakahPrima.py import *")
from apakahPrima import *
$(ccetak "$(prt "[x for x in range(20,50) if apakahPrima(x)]")")
$(prt "[x for x in range(20,50) if apakahPrima(x)]")

END

echo " "
echo "Keluar dari shell interaktif Python."