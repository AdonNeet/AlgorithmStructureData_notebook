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
$(ccetak "from linearSearch import *")
from linearSearch import *
$(ccetak "A = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]")
A = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
$(ccetak "cari(A, 31)")
cari(A, 31)
$(ccetak "$(prt "cariLurus(A, 31)")")
$(prt "cariLurus(A, 31)")
$(ccetak "$(prt "cariLurus(A, 8)")")
$(prt "cariLurus(A, 8)")
END

echo " "
echo "Keluar dari shell interaktif Python."