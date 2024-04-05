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
a="head"
b="second"
c="third"
d="tail"

# Menampilkan pesan penggunaan
echo "Memulai skrip isi shell interaktif Python..."
echo " "

# Memulai shell interaktif Python
python << END

$(ccetak "from dnode import *")
from dnode import *
$(ccetak " ")
$(ccetak "# Membuat linked list awal dengan data 1, 2, 3, 4")
$(ccetak "${a} = DNode(1)")
${a} = DNode(1)
$(ccetak "${b} = DNode(2)") 
${b} = DNode(2)
$(ccetak "${c} = DNode(3)")
${c} = DNode(3)
$(ccetak "${d} = DNode(4)")
${d} = DNode(4)

$(ccetak " ")
$(ccetak "${a}.next = ${b}")
${a}.next = ${b}
$(ccetak "${b}.prev = ${a}")
${b}.prev = ${a}
$(ccetak "${b}.next = ${c}")
${b}.next = ${c}
$(ccetak "${c}.prev = ${b}")
${c}.prev = ${b}
$(ccetak "${c}.next = ${d}")
${c}.next = ${d}
$(ccetak "${d}.prev = ${c}")
${d}.prev = ${c}

$(ccetak " ")

$(ccetak "# Menampilkan isi linked list dari depan")
$(ccetak "kunjungi_depan(${a})")
kunjungi_depan(${a})

$(ccetak " ")

$(ccetak "# Menampilkan isi linked list dari belakang")
$(ccetak "kunjungi_belakang(${d})")
kunjungi_belakang(${d})

$(ccetak " ")

$(ccetak "# Menambahkan simpul baru di awal linked list dengan data 0")
$(ccetak "${a} = tambahDepan(${a}, 0)")
${a} = tambahDepan(${a}, 0)
$(ccetak "kunjungi_depan(${a})")
kunjungi_depan(${a})

$(ccetak " ")

$(ccetak "# Menambahkan simpul baru di akhir linked list dengan data 5")
$(ccetak "${d} = tambahAkhir(${d}, 5)")
${d} = tambahAkhir(${d}, 5)
$(ccetak "kunjungi_depan(${a})")
kunjungi_depan(${a})

END

echo " "
echo "Keluar dari shell interaktif Python."