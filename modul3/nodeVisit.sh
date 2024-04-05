#!/bin/bash

# Menampilkan pesan penggunaan
echo "Memulai skrip isi shell interaktif Python..."
echo " "


# Memulai shell interaktif Python
python << END
# Masukkan skrip dibawah ini
print(">>> from node import *")
from node import *
print(">>> a = Node(11)")
a = Node(11)
print(">>> b = Node(52)")
b = Node(54)
print(">>> c = Node(18)")
c = Node(18)

print(">>> ")

print(">>> a.next = b")
a.next = b
print(">>> b.next = c")
b.next = c

print(">>> ")

print(">>> print(a.data)")
print(a.data)
print(">>> print(a.next.data)")
print(a.next.data)
print(">>> print(a.next.next.data)")
print(a.next.next.data)

print(">>> ")

print(">>> kunjungi(a)")
kunjungi(a)

END

echo " "
echo "Keluar dari shell interaktif Python."
