#!/bin/bash

# Menampilkan pesan penggunaan
echo "Memulai skrip isi shell interaktif Python..."
echo " "


# Memulai shell interaktif Python
python << END
# Masukkan skrip dibawah ini
print(">>> B = [[0 for j in range(3)] for i in range(3)]")
B = [[0 for j in range(3)] for i in range(3)]
print(">>> B")
print(B)

END

echo " "
echo "Keluar dari shell interaktif Python."
