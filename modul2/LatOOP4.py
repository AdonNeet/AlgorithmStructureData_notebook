class Manusia(object):
    """ Class 'Manusia' dengan inisiasi 'nama' """
    keadaan = 'lapar'

    def __init__(self, nama):
        self.nama = nama

    def ucapkanSalam(self):
        print("Salaam, namaku", self.nama)

    def makan(self, s):
        print("Saya baru saja makan", s)
        self.keadaan = 'kenyang'

    def olahraga(self, k):
        print("Saya baru saja latihan", k)
        self.keadaan = 'lapar'

    def mengalikanDenganDua(self, n):
        return n * 2

class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dari class Manusia."""
    def __init__(self, nama, NIM, kota, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia."""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    
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

