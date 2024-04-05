# L200220194
from math import sqrt as akar

def rerata(b):
    n = 0;
    tempA = 0;
    for i in b:
        tempA += i;
        n += 1;
    return tempA/n;

def varians(b):
    n = 0;
    tempA = 0;
    mean = rerata(b);
    for i in b:
        tempA += (i - mean)**2;
        n += 1;
    return tempA/n;

def standarDeviasi(b):
    n = 0;
    tempA = 0;
    for i in b:
        tempA += i**2;
        n += 1;
    return akar(tempA/n);

