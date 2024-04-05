from arrayMhs import *

def insertionSortNIM(A):
    n = len(A.data)
    for i in range(1, n):
        nim = int(A[i, 'NIM'])  # Menggunakan __getitem__ untuk mengakses NIM
        tmp = A[i]
        pos = i
        while pos > 0 and nim < int(A[pos - 1, 'NIM']):  # Perbandingan nilai berdasarkan NIM
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = tmp
    # return A


