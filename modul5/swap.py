def swap(A, p, q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

if __name__ == "__main__":
    K = [50, 20, 70, 10]
    print("Before\n", K, "\n")
    swap(K, 1, 3)
    print("After\n", K)