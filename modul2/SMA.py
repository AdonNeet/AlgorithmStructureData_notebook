# L200220194
from LatOOP3 import *

class SiswaSMA(Manusia):
    def __init__(self, nama, NIM, major, kota, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia."""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
        self.jurusan = major
        self.hobi = []
    def __str__(self):
        s = 'Nama ' + self.cekNama() + ', NIM ' + str(self.cekNIM()) \
            + '. Tinggal di ' + self.cekKotaTinggal() \
            + '. Jurusan ' + self.cekJurusan() \
            + '. Uang saku Rp ' + str(self.cekUangSaku()) \
            + ' tiap bulannya.'
        return s
    def cekNama(self):
        return self.nama
    def cekNIM(self):
        return self.NIM
    def cekKotaTinggal(self):
        return self.kotaTinggal
    def gantiTempat(self, kota):
        self.kotaTinggal = kota
    def cekUangSaku(self):
        return self.uangSaku
    def addUangSaku(self, n):
        self.uangSaku += n
    def cekJurusan(self):
        return self.jurusan
    def addHobi(self, keg):
        self.hobi = self.hobi + [str(keg)]
    def delHobi(self, keg):
        self.hobi.remove(str(keg))  

