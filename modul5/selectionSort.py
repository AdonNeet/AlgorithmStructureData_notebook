def swap(A, p, q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiYangTerkecil = dariSini           #-> anggap ini yang terkecil
    for i in range(dariSini, sampaiSini):   #-> cari di sisa list
        if A[i] < A[posisiYangTerkecil]:    #-> kalau menemukan yang lebih kecil,
            posisiYangTerkecil = i          #-> anggapan dirubah
    return posisiYangTerkecil

def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i:
            swap(A, i, indexKecil)

if __name__ == "__main__":
    L = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
    print("Before:\n", L)
    selectionSort(L)
    print("After:\n", L)