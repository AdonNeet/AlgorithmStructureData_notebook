# L200220194
from LatOOP3 import *

class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dari class Manusia."""
    def __init__(self, nama, NIM, kota, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia."""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
        self.listKuliah = []

    def __str__(self):
        s = self.nama + ', NIM ' + str(self.NIM) \
            + '. Tinggal di ' + self.kotaTinggal \
            + '. Uang saku Rp ' + str(self.uangSaku) \
            + ' tiap bulannya.'
        return s

    def ambilNama(self):
        return self.nama

    def ambilNIM(self):
        return self.NIM

    def ambilUangSaku(self):
        return self.uangSaku

    def makan(self, s):
        """Metode ini menutupi metode 'makan' dari class Manusia.
        Mahasiswa makan sambil belajar."""
        print("Saya baru saja makan", s, "sambil belajar.")
        self.keadaan = 'kenyang'

    def ambilKotaTinggal(self):
        return self.kotaTinggal

    def perbaruiKotaTinggal(self, kota):
        self.kotaTinggal = kota

    def tambahUangSaku(self, uang):
        self.uangSaku += uang

    def ambilKuliah(self, mk):
        mk = str(mk)
        self.listKuliah = self.listKuliah + [mk]

    def hapusKuliah(self, mk):
        mk = str(mk)
        self.listKuliah.remove(mk)

class MhsTIF(Mahasiswa):  # Perhatikan class induknya: Mahasiswa
    """Class MhsTIF yang dibangun dari class Mahasiswa"""
    def katakanPy(self):
        print('Python is cool.')

