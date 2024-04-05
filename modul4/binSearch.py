# Quicksort dengan pendekatan list comprehension, efisiensi 50%
def quicksort(arr):
	if len(arr) <= 1:
		return arr
	else:
		pivot = arr[0]
		left = [x for x in arr[1:] if x < pivot]
		right = [x for x in arr[1:] if x >= pivot]
		return quicksort(left) + [pivot] + quicksort(right)

def binSe(kumpulan, target):
    # Mulai dari seluruh runtutan elemen
    low = 0
    high = len(kumpulan) - 1

    # Secara berulang belah runtutan itu menjadi separuhnya
    # sampai target ditemukan
    while low <= high:
        # Temukan pertengahan runtut itu
        mid = (high + low) // 2
        # Apakah pertengahannya memuat target?
        if kumpulan[mid] == target:
            return True
        # Ataukah targetnya di sebelah kirinya?
        elif target < kumpulan[mid]:
            high = mid - 1
        # ataukah targetnya di sebelah kanannya?
        else:
            low = mid + 1
    #Jika runtutanya tidak bisa dibelah lagi, berarti targetnya tidak ada
    return False
      
# Tugas 6 dan 7
def binSeIDX(kumpulan, target):     # minusnya hanya mendeteksi satu angka saja
    low = 0
    high = len(kumpulan) - 1
    while low <= high:
        mid = (high + low) // 2
        if kumpulan[mid] == target:
            return [mid]
        elif target < kumpulan[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

def binSea(kumpulan, target):
    # Mulai dari seluruh runtutan elemen
    low = 0
    high = len(kumpulan) - 1
    post = []

    # Secara berulang belah runtutan itu menjadi separuhnya
    # sampai target ditemukan
    while low <= high:
        # Temukan pertengahan runtut itu
        mid = (high + low) // 2
        # Apakah pertengahannya memuat target?
        if kumpulan[mid] == target:
            # Mencari indeks di sebelah kiri dari pertengahan yang memiliki nilai target
            left_index = mid
            while left_index >= 0 and kumpulan[left_index] == target:
                post.append(left_index)
                left_index -= 1
            # Mencari indeks di sebelah kanan dari pertengahan yang memiliki nilai target
            right_index = mid + 1
            while right_index < len(kumpulan) and kumpulan[right_index] == target:
                post.append(right_index)
                right_index += 1
            return post
        # Ataukah targetnya di sebelah kirinya?
        elif target < kumpulan[mid]:
            high = mid - 1
        # ataukah targetnya di sebelah kanannya?
        else:
            low = mid + 1
    
    #Jika runtutanya tidak bisa dibelah lagi, berarti targetnya tidak ada
    if len(post) != 0:
        return post
    else:
        return False

# Contoh penggunaan
# kumpulan = [2, 3, 5, 6, 6, 6, 8, 9, 9, 10, 11, 12, 13, 13, 14]
# target = 6
# print(binSe(kumpulan, target))



