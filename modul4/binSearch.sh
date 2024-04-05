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
hallo="Hello World!"

# Menampilkan pesan penggunaan
echo "Memulai skrip isi shell interaktif Python..."
echo " "

# Memulai shell interaktif Python
python << END
$(ccetak "from binSearch import *")
from binSearch import *
$(ccetak "arr = [1, 7, 4, 1, 10, 9, -2]")
arr = [1, 7, 4, 1, 10, 9, -2]
$(ccetak "sorted_arr = quicksort(arr)  # Sorted Array dalam urutan meningkat")
sorted_arr = quicksort(arr)
$(ccetak "$(prt "sorted_arr")")
print(sorted_arr)
$(ccetak "cek = binSe(sorted_arr, -2) # Cek -2 dalam arr")
cek = binSe(sorted_arr, -2)
$(ccetak "$(prt "cek")")
$(prt "cek")

END

echo " "
echo "Keluar dari shell interaktif Python."