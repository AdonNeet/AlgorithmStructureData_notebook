#!/bin/bash

# fungsi cetak(x) di dalam skrip Bash
prt () {
    echo "print(${1})"
}

cetak() {
        echo "print('${1}')"
}

ccetak() {      # ini untuk mencetak print didalam print
        echo "print(\">>> ${1}\")"
}

# Simpan kalimat atau perintah yang mungkin dijalankan berulang
a="A = [[2,3], [5,7]]"
b="A[0][1]"
c="A[1][1]"

# Menampilkan pesan penggunaan
echo "Memulai skrip isi shell interaktif Python..."
echo " "

# Memulai shell interaktif Python
python << END
# Masukkan skrip dibawah ini
$(ccetak "$(cetak "${a}")")
A = [[2,3], [5,7]]
$(ccetak "$(cetak "${b}")")
$(prt "${b}")
$(ccetak "$(cetak "${c}")")
$(prt "${c}")


END

echo " "
echo "Keluar dari shell interaktif Python."
