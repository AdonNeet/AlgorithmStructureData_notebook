#!/bin/bash

# fungsi cetak(x) di dalam skrip Bash
cetak() {
        echo "print('${1}')"
}

ccetak() {      # ini untuk mencetak print didalam print
        echo "print(\">>> ${1}\")"
}

# Simpan kalimat atau perintah yang mungkin dijalankan berulang
a1="Hello World!"

# Menampilkan pesan penggunaan
echo "Memulai skrip isi shell interaktif Python..."
echo " "

# Memulai shell interaktif Python
python << END
# Masukkan skrip di bawah ini
${a1}
END

echo " "
echo "Keluar dari shell interaktif Python."