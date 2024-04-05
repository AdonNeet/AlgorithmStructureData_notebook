import sys
sys.path.append('../modul2') 
from dataMhs import *

class daftarMhs:
    def __init__(self, src=None, nama=None, nim=None, kota=None, us=None):
        self.data = []
        if all(arg is not None for arg in (src, nama, nim, kota)):
            us = kota
            kota = nim
            nim = nama
            nama = src
            self.data.append(MhsTIF(nama, nim, kota, us))
        elif all(arg is not None for arg in (src, nama, nim, kota, us)):
            self.data.append(MhsTIF(nama, nim, kota, us)) 
        elif src is not None:
            if isinstance(src, MhsTIF):
                self.data.append(src)
            elif isinstance(src, list):
                if isinstance(src[0], MhsTIF):
                    self.data.extend(src)
                elif isinstance(src[0], tuple):
                    for i in src:
                        self.data.append(MhsTIF(*i))
                else:
                    print("Data tidak bisa dimasukkan")
            else:
                print("Data tidak bisa dimasukkan")
        

    def __getitem__(self, key=None):
        results = []
        if(key != None):
            for mhs in self.data:
                try:
                    value = getattr(mhs, key)
                    results.append(value)
                except AttributeError:
                    pass
            return results
        else:
            return [mhs for mhs in self.data]
        
    def __getattr__(self, key="None"):
        if all(hasattr(mhs, key) for mhs in self.data) :
            return [getattr(mhs, key, None) for mhs in self.data]
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{key}'")
        
    def __repr__(self):
        return repr([vars(mhs) for mhs in self.data])


# Contoh penggunaan
# dm1 = daftarMhs(src)  # untuk menginisialisasi dengan sumber data src
# dm2 = daftarMhs("Adon", 30, "Kudus", 10000)  # untuk menginisialisasi dengan data individu
# print(dm2['nama'])