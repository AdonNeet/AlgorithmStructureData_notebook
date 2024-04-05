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

$(ccetak "from node import *")
from node import *
$(ccetak "head = Node(1)")
head = Node(1)
$(ccetak "head.next = Node(2)")
head.next = Node(2)
$(ccetak "head.next.next = Node(3)")
head.next.next = Node(3)
$(ccetak "head.next.next.next = Node(4)")
head.next.next.next = Node(4)

$(ccetak " ")

$(ccetak "# isi linked list awal")
$(ccetak "kunjungi(head)")
kunjungi(head)

$(ccetak " ")

$(ccetak "# Mencari data tertentu dalam linked list")
$(ccetak "data_cari = 3")
data_cari = 3
$(ccetak "hasil_cari = cari(head, data_cari)")
hasil_cari = cari(head, data_cari)
$(ccetak "$(prt "hasil_cari.data")")
$(prt "hasil_cari.data")

$(ccetak " ")

$(ccetak "# Menambahkan simpul baru di awal linked list dengan data 0")
$(ccetak "head = tambahDepan(head, 0)")
head = tambahDepan(head, 0)
$(ccetak "kunjungi(head)")
kunjungi(head)


$(ccetak " ")

$(ccetak "# Menambahkan simpul baru di akhir linked list dengan data 5")
$(ccetak "head = tambahAkhir(head, 5)")
head = tambahAkhir(head, 5)
$(ccetak "kunjungi(head)")
kunjungi(head)

$(ccetak " ")

$(ccetak "# Menyisipkan simpul baru dengan data 3.5 setelah simpul dengan data 3")
$(ccetak "head = tambah(head, 3.5, 3)")
head = tambah(head, 3.5, 3)
$(ccetak "kunjungi(head)")
kunjungi(head)

$(ccetak " ")

$(ccetak "# Menghapus simpul pertama dari linked list")
$(ccetak "head = hapus(head, 0)")
head = hapus(head, 0)
$(ccetak "kunjungi(head)")
kunjungi(head)

$(ccetak " ")

$(ccetak "# Menghapus simpul terakhir dari linked list")
$(ccetak "head = hapus(head,5)")
head = hapus(head,5)
$(ccetak "kunjungi(head)")
kunjungi(head)

$(ccetak " ")

$(ccetak "# Menghapus simpul dengan data 3.5 dari linked list")
$(ccetak "head = hapus(head, 3)")
head = hapus(head, 3)
$(ccetak "kunjungi(head)")
kunjungi(head)

END

echo " "
echo "Keluar dari shell interaktif Python."