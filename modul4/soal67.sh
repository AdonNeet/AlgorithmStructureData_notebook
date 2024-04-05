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
$(ccetak "from binSearch import *")
from binSearch import *
$(ccetak "arr1 = [1, 7, 4, 1, 10, 9, -2]")
arr1 = [1, 7, 4, 1, 10, 9, -2]
$(ccetak "sorted_arr = quicksort(arr1)  # Sorted Array dalam urutan meningkat")
sorted_arr = quicksort(arr1)
$(ccetak "$(prt "sorted_arr")")
print(sorted_arr)
$(ccetak "cek1 = binSea(sorted_arr, 4) # Cek 4 dalam arr")
cek1 = binSea(sorted_arr, 4)
$(ccetak "$(prt "cek1")")
$(prt "cek1")
$(ccetak "cek2 = binSea(sorted_arr, 1) # Cek 1 dalam arr")
cek2 = binSea(sorted_arr, 1)
$(ccetak "$(prt "cek2")")
$(prt "cek2")
$(ccetak " ")
$(ccetak "arr2 = [2, 3, 5, 6, 6, 6, 8, 9, 9, 10, 11, 12, 13, 13, 14]")
arr2 = [2, 3, 5, 6, 6, 6, 8, 9, 9, 10, 11, 12, 13, 13, 14]
$(ccetak "target = 6")
target = 6
$(ccetak "cek3 = binSea(arr2, target) # Cek 6 dalam arr")
cek3 = binSea(arr2, target)
$(ccetak "$(prt "cek3")")
$(prt "cek3")

END

echo " "
echo "Keluar dari shell interaktif Python."