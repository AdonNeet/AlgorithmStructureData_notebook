def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:   # -> Cari posisi yang tepat
            A[pos] = A[pos - 1] # dan geser ke kanan terus
            pos = pos - 1       # nilai-nilai yang lebih besar
        A[pos] = nilai # -> Pada posisi ini tempatkan nilai elemen ke i.

if __name__ == "__main__":
    L = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
    print("Before:\n", L)
    insertionSort(L)
    print("After:\n", L)