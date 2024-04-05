import random

def tebak100():
    # Membangkitkan angka random antara 1 sampai 100
    angka_rahasia = random.randint(1, 100)

    print("Permainan tebak angka.")
    print("Saya menyimpan sebuah angka bulat antara 1 sampai 100. Coba tebak.")

    # Menebak angka
    tebakan_ke = 0
    found = False
    while tebakan_ke < 8:
        tebakan_ke += 1
        tebakan = int(input(f"Masukkan tebakan ke-{tebakan_ke}:> "))

        if tebakan < angka_rahasia:
            print("Itu terlalu kecil. Coba lagi.")
        elif tebakan > angka_rahasia:
            print("Itu terlalu besar. Coba lagi.")
        else:
            print("Ya. Anda benar.\n\n")
            found = not found
            break
    if(found != True):
        print("Anda gagal untuk menebak angka.\n\n")

def tebak1000():
    # Membangkitkan angka random antara 1 sampai 100
    angka_rahasia = random.randint(1, 1000)

    print("Permainan tebak angka.")
    print("Saya menyimpan sebuah angka bulat antara 1 sampai 1000. Coba tebak.")

    # Menebak angka
    tebakan_ke = 0
    found = False
    while tebakan_ke < 11:
        tebakan_ke += 1
        tebakan = int(input(f"Masukkan tebakan ke-{tebakan_ke}:> "))

        if tebakan < angka_rahasia:
            print("Itu terlalu kecil. Coba lagi.")
        elif tebakan > angka_rahasia:
            print("Itu terlalu besar. Coba lagi.")
        else:
            print("Ya. Anda benar.\n\n")
            found = not found
            break
    if(found != True):
        print("Anda gagal untuk menebak angka.\n\n")
    

if __name__ == "__main__":
    tebak100()
    # tebak1000()
