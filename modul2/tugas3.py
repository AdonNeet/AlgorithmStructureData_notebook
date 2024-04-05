# L200220194
from dataMhs import *

def masukkan():
    print(
            "Program input data mahasiswa secara interaktif" \
            + "Silahkan masukkan data yang diminta :D"
          )
    nama = str(input("Masukkan nama      : "))
    nim =      input("Masukkan nim       : ")
    kota = str(input("Masukkan kota      : "))
    n =        input("Masukkan uang saku : ")
    tempA = Mahasiswa(nama, nim, kota, n)
    print("\nBerikut merupakan data mahasiswa yang telah dimasukkan")
    print(tempA)
    return tempA


def main():
    global m1
    m1 = masukkan()
    

if __name__ == "__main__":
    main()
