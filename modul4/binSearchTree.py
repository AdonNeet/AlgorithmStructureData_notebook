import matplotlib.pyplot as plt
import math

def rounded_log2(x):
    result = math.log(x, 2)  # Menghitung logaritma basis 2 dari x
    rounded_result = math.ceil(result) # bulatkan ke atas
    return rounded_result

def draw_binary_search_tree(low, high, parent_x, parent_y, x_offset, y_offset, level):
    if low > high:
        return
    
    # hitung posisi node sekarang
    x = (low + high) // 2
    y = depth - level  
    
    # gambar node sekarang
    plt.text(x, y, str(x), ha='center', bbox=dict(facecolor='white', edgecolor='none', boxstyle='circle'))
    
    # Draw edge to parent
    if parent_x is not None:
        plt.plot([parent_x, x], [parent_y, y], 'bo-')
    
    # Pemanggilan rekursi untuk anak sebelah kanan dan kiri
    draw_binary_search_tree(low, x - 1, x, y, x_offset / 2, y_offset, level + 1)
    draw_binary_search_tree(x + 1, high, x, y, x_offset / 2, y_offset, level + 1)

def main():
    print("Note: \ndisarankan jarak angka tidak terlalu jauh\n")
    low = int(input("Masukkan batas bawah: "))  # Batas bawah
    high = int(input("Masukkan batas atas: "))  # Batas atas, semakin banyak jumlah angka semakin tidak terlihat pohon-nya
    global depth
    depth = rounded_log2((high-low)+1)
    plt.figure(figsize=(10, 6))
    draw_binary_search_tree(low, high, None, 6, 2, 2, 1)  # level dimulai dari 1
    plt.title('Binary Search Tree')
    plt.xlabel('Value')
    plt.ylabel('Level')
    plt.gca().invert_yaxis()  # Flip y-axis to start from top
    plt.show()

if __name__ == "__main__":
    main()
