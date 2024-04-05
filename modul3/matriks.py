# L200220194
# Tugas 1
class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])
 
    def shape(self):
        return (self.rows, self.cols)
 
    def is_consistent(self, other):
        return self.shape() == other.shape()
 
    def add(self, other):
        if not self.is_consistent(other):
            raise ValueError("Ukuran matriks tidak konsisten")
 
        result = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                result[i][j] = self.data[i][j] + other.data[i][j]
        return Matrix(result)
 
    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Jumlah kolom pada matriks pertama harus sama dengan jumlah baris pada matriks kedua")
 
        result = [[0 for _ in range(other.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(result)
 
    def determinant(self):
        if self.rows != self.cols:
            raise ValueError("Matriks harus memiliki jumlah kolom dan baris yang sama")
 
        if self.rows == 1:
            return self.data[0][0]
        elif self.rows == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
        else:
            det = 0
            for i in range(self.cols):
                minor = self.get_minor(0, i)
                det += ((-1) ** i) * self.data[0][i] * minor.determinant()
            return det
 
    def get_minor(self, row, col):
        minor_data = [row[:col] + row[col + 1:] for row in (self.data[:row] + self.data[row + 1:])]
        return Matrix(minor_data)
 
    def __repr__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

#Tugas 2
def buatNol(m, n=None):
    if n is None:
        n = m
    return Matrix([[0 for _ in range(n)] for _ in range(m)])

def buatIdentitas(m):
    return Matrix([[1 if i == j else 0 for j in range(m)] for i in range(m)])

# Contoh penggunaan:
# print("Matrix berisi nol:")
# print(buatNol(3, 4))  # Matrix 3x4 berisi nol
# print(buatNol(2))      # Matrix 2x2 berisi nol (bujur sangkar)

# print("\nMatrix identitas:")
# print(buatIdentitas(3))  # Matrix identitas 3x3
# print(buatIdentitas(4))  # Matrix identitas 4x4
