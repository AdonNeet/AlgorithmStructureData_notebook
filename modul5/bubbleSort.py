def swap(A, p, q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def bubbleSort(A):
    n = len(A)
    for i in range(n-1):        #-> Lakukan operasi gelembung sebanyak n-1
        for j in range(n-i-1):  #-> Dorong elemen terbesar ke ujung kanan
            if A[j] > A[j+1]:   #-> Jika di kiri lebih besar dari di kanannya,
                swap(A,j,j+1)   #-> tukar posisi elemen ke j dengan ke j+1

if __name__ == "__main__":
    L = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
    print("Before:\n", L)
    bubbleSort(L)
    print("After:\n", L)