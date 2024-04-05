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
a="buatNol(3, 4)"
b="buatNol(2)"
c="buatIdentitas(3)"
d="buatIdentitas(4)"

# Menampilkan pesan penggunaan
echo "Memulai skrip isi shell interaktif Python..."
echo " "

# Memulai shell interaktif Python
python << END

$(ccetak "from matriks import *")
from matriks import *
# $(ccetak "# Matrix berisi nol")
$(ccetak "$(prt "${a}")")
$(prt "${a}")  # Matrix 3x4 berisi nol
$(ccetak "$(prt "${b}")")
$(prt "${b}")      # Matrix 2x2 berisi nol (bujur sangkar)
# $(ccetak "# Matrix identitas")
$(ccetak "$(prt "${c}")")
$(prt "${c}")  # Matrix identitas 3x3
$(ccetak "$(prt "${d}")")
$(prt "${d}")  # Matrix identitas 4x4

END

echo " "
echo "Keluar dari shell interaktif Python."