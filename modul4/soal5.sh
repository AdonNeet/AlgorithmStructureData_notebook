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
$(ccetak "from linkedList import *")
from linkedList import *
$(ccetak "# Membuat linked list, tidak boleh memiliki element dengan nilai yang sama")
$(ccetak "linked_list = LinkedList(Node(3, Node(7, Node(9, Node(11, Node(30, Node(-2, Node(10, Node(5)))))))))")
linked_list = LinkedList(Node(3, Node(7, Node(9, Node(11, Node(30, Node(-2, Node(10, Node(5)))))))))
$(ccetak "linked_list.PrintLinkedList()")
linked_list.PrintLinkedList()
$(ccetak "linked_list.Search(-2)")
linked_list.Search(-2)
END

echo " "
echo "Keluar dari shell interaktif Python."