def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiYangTerkecil = dariSini           #-> anggap ini yang terkecil
    for i in range(dariSini, sampaiSini):   #-> cari di sisa list
        if A[i] < A[posisiYangTerkecil]:    #-> kalau menemukan yang lebih kecil,
            posisiYangTerkecil = i          #-> anggapan dirubah
    return posisiYangTerkecil

if __name__ == "__main__":
    A = [18, 13, 44, 25, 66, 107, 78, 89]
    j = cariPosisiYangTerkecil(A, 2, len(A))
    print("Posisi idx nilai terkecil mulai dari idx 2:\n", j)