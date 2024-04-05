def cari(data, tar):
    if tar in data:
        print("targetnnya terdapat di array itu.")
    else:
        print("targetnua tidak terdapat di array itu.")

def cariLurus(wadah, target):
    n = len(wadah)
    for i in range(n):
        if wadah[i] == target:
            return True
        return False

# A = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
# cari(A, 31)
