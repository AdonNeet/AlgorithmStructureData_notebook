from listMhs import *

def cariKota(objek, target):
    printed = set()
    for mhs in objek.data:
        if mhs.kotaTinggal == target and mhs.nama not in printed:
            print(mhs.nama, 'tinggal di', target)
            printed.add(mhs.nama)

# Tugas 1 - 4
def cariKotaIDX(objek, target):
    founded = []
    for i in range(0, len(objek.data)):
        if objek.data[i].kotaTinggal == target:
            founded.append(i)
    print(list(founded))

def sakuKecil(objek):
    pos = 0
    for i in range(0, len(objek.data)):
        if i == 0:
            continue
        else:
            if objek.data[i].uangSaku < objek.data[pos].uangSaku:
                pos = i
    print("Uang saku paling terkecil", objek.data[pos].uangSaku)

def sakuBesar(objek):
    pos = 0
    for i in range(0, len(objek.data)):
        if i == 0:
            continue
        else:
            if objek.data[i].uangSaku > objek.data[pos].uangSaku:
                pos = i
    print("Uang saku paling terbesar", objek.data[pos].uangSaku, "pada mahasiswa bernama", objek.data[pos].nama)

def mhsLowest(objek):
    founded = []
    pos = 0
    for i in range(0, len(objek.data)):
        if i == 0:
            continue
        else:
            if objek.data[i].uangSaku < objek.data[pos].uangSaku:
                pos = i
    for mhs in objek.data:
        if mhs.uangSaku == objek.data[pos].uangSaku:
            founded.append(vars(mhs))
    print(founded)

def kurangDari(objek, uang):
    founded = []
    for i in range(0, len(objek.data)):
        if objek.data[i].uangSaku < uang:
            founded.append(objek.data[i].nama)
        else:
            continue
    print(founded)

def lebihDari(objek, uang):
    founded = []
    for i in range(0, len(objek.data)):
        if objek.data[i].uangSaku >= uang:
            founded.append(objek.data[i].nama)
        else:
            continue
    print(founded)

