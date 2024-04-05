# L200220194
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

# Kelas Mahasiswa
class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dari class Manusia."""
    def __init__(self, nama, NIM, kota, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia."""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
        self.listKuliah = []

    def __getitem__(self, key=None):
        if key is None:
            return vars(self)
        else:
            return getattr(self, key)


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

# Array Mahasiswa
class daftarMhs:
    def __init__(self, src=None, nama=None, nim=None, kota=None, us=None):
        self.data = []
        self.count = 0
        if all(arg is not None for arg in (src, nama, nim, kota)):
            us = kota
            kota = nim
            nim = nama
            nama = src
            self.data.append(MhsTIF(nama, nim, kota, us))
            self.count += 1
        elif all(arg is not None for arg in (nama, nim, kota, us)):
            self.data.append(MhsTIF(nama, nim, kota, us)) 
            self.count += 1
        elif src is not None:
            if isinstance(src, MhsTIF):
                self.data.append(src)
                self.count += 1
            elif isinstance(src, list):
                if isinstance(src[0], MhsTIF):
                    self.data.extend(src)
                    self.count += len(src)
                elif isinstance(src[0], tuple):
                    for i in src:
                        self.data.append(MhsTIF(*i))
                        self.count += 1
                else:
                    print("Data tidak bisa dimasukkan")
            else:
                print("Data tidak bisa dimasukkan")

    def __setitem__(self, index, value):    
        if 0 <= index < len(self.data):
            self.data[index] = value  
        else:
           raise IndexError("Indeks diluar rentang array mahasiswa")
        
    def __getitem__(self, key=None):
        results = []
        index = val = None
        if(isinstance(key, tuple)):
            index, val = key
        if(isinstance(key, int)):
            return self.data[key]
        elif(isinstance(key, str)):
            for mhs in self.data:
                try:
                    value = getattr(mhs, key)
                    results.append(value)
                except AttributeError:
                    pass
            return results
        elif(index != None and isinstance(index, int) and isinstance(val, str)):
            rest = None
            try:
                value = getattr(self.data[index], val)
                rest = value
            except AttributeError:
                pass
            return rest
        else:
            return [vars(mhs) for mhs in self.data]
        
    def __getattr__(self, key="None"):
        if all(hasattr(mhs, key) for mhs in self.data) :
            return [getattr(mhs, key, None) for mhs in self.data]
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{key}'")
        
    def __repr__(self):
        return repr([vars(mhs) for mhs in self.data])

    def __sizeof__(self):
        return len(self.data)


