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
c0="MhsTIF('Ika', 10, 'Sukoharjo', 240000)"
c1="MhsTIF('Budi', 51, 'Sragen', 230000)"
c2="MhsTIF('Ahmad', 2, 'Surakarta', 250000)"
c3="MhsTIF('Chandra', 18, 'Surakarta', 235000)"
c4="MhsTIF('Eka', 4, 'Boyolali', 240000)"
c5="MhsTIF('Fandi', 31, 'Salatiga', 250000)"
c6="MhsTIF('Deni', 13, 'Klaten', 245000)"
c7="MhsTIF('Galuh', 5, 'Wonogiri', 245000)"
c8="MhsTIF('Janto', 23, 'Klaten', 245000)"
c9="MhsTIF('Hasan', 64, 'Karanganyar', 270000)"
c10="MhsTIF('Khalid', 29, 'Purwodadi', 265000)"

# Menampilkan pesan penggunaan
echo "Memulai skrip isi shell interaktif Python..."
echo " "

# Memulai shell interaktif Python
python << END
$(ccetak "from cariMhs import *")
from cariMhs import *
$(ccetak "c0 = $c0")
c0 = $c0
$(ccetak "c1 = $c1")
c1 = $c1
$(ccetak "c2 = $c2")
c2 = $c2
$(ccetak "c3 = $c3")
c3 = $c3
$(ccetak "c4 = $c4")
c4 = $c4
$(ccetak "c5 = $c5")
c5 = $c5
$(ccetak "c6 = $c6")
c6 = $c6
$(ccetak "c7 = $c7")
c7 = $c7
$(ccetak "c8 = $c8")
c8 = $c8
$(ccetak "c9 = $c9")
c9 = $c9
$(ccetak "c10 = $c10")
c10 = $c10
$(ccetak " ")
$(ccetak "n = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]")
n = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]
$(ccetak "daftar = daftarMhs(n)")
daftar = daftarMhs(n)
$(ccetak "$(prt "daftar")")
$(prt "daftar")
$(ccetak " ")
$(ccetak "cariKota(daftar, 'Klaten')")
cariKota(daftar, 'Klaten')
$(ccetak "sakuKecil(daftar)")
sakuKecil(daftar)
$(ccetak "sakuBesar(daftar)")
sakuBesar(daftar)
$(ccetak "kurangDari(daftar, 250000)")
kurangDari(daftar, 250000)
$(ccetak "lebihDari(daftar, 250000)")
lebihDari(daftar, 250000)

# for obj in daftar.data: # output berupa __str__ objek didalam list
#     print(obj)

END

echo " "
echo "Keluar dari shell interaktif Python."