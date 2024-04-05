from math import sqrt as akar

def selesaikanABC(a,b,c):
    a = float(a) # mengubah jenis integer menjadi float
    b = float(b)
    c = float(c)
    D = b**2 - 4*a*c
    x1 = (-b + akar(D))/(2*a)
    x2 = (-b - akar(D))/(2*a)
    hasil = (x1,x2) # tuple yang terdiri dari dua elemen
    return hasil
