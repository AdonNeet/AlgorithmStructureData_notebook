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
a="m1 = Matrix([[1, 2, 3], [4, 5, 6]])"
b="m2 = Matrix([[7, 8, 9], [10, 11, 12]])"
c="m1"
d="m2"
e="m3 = Matrix([[1, 2], [3, 4], [5, 6]])"
f="m4 = Matrix([[7, 8], [9, 10]])"
ee="m3"
ff="m4"
g="m5 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])"
gg="m5"

# Menampilkan pesan penggunaan
echo "Memulai skrip isi shell interaktif Python..."
echo " "

# Memulai shell interaktif Python
python << END

$(ccetak "from matriks import *")
from matriks import *
$(ccetak "${a}")
${a}
$(ccetak "${b}")
${b}
$(ccetak "$(prt "${c}")")
$(prt "${c}")
$(ccetak "$(prt "${d}")")
$(prt "${d}")

$(ccetak "# Ukuran matriks 1 dan 2")
$(ccetak "${c}.shape()")
$(prt "${c}.shape()")
$(ccetak "${d}.shape()")
$(prt "${d}.shape()")

$(ccetak " ")
$(ccetak "# Penjumlahan Matriks")
$(ccetak "${c}.add(${d})")
$(prt "${c}.add(${d})")

$(ccetak " ")
$(ccetak "${e}")
${e}
$(ccetak "${f}")
${f}
$(ccetak "# Perkalian Matriks")
$(ccetak "${ee}.multiply(${ff})")
$(prt "${ee}.multiply(${ff})")

$(ccetak " ")
$(ccetak "${g}")
${g}
$(ccetak "# Determinan matriks")
$(ccetak "${gg}.determinant()")
$(prt "${gg}.determinant()")

END

echo " "
echo "Keluar dari shell interaktif Python."