class Pesan(object):
    """
    Sebuah class bernama Pesan.
    Untuk memahami konsep Class dan Object.
    """
    def __init__(self, sebuahString):
        self.teks = sebuahString
    
    def cetakIni(self):
        print(self.teks)
    
    def cetakPakaiHurufKapital(self):
        print(self.teks.upper())
    
    def cetakPakaiHurufKecil(self):
        print(self.teks.lower())
    
    def jumKar(self):
        return len(self.teks)
    
    def cetakJumlahKarakterku(self):
        print('Kalimatku mempunyai', len(self.teks), 'karakter.')
    
    def perbarui(self, stringBaru):
        self.teks = stringBaru

# Contoh penggunaan:
# pesan = Pesan("Contoh pesan")
# pesan.cetakIni()
# pesan.cetakPakaiHurufKapital()
# pesan.cetakPakaiHurufKecil()
# print("Jumlah karakter:", pesan.jumKar())
# pesan.cetakJumlahKarakterku()
# pesan.perbarui("Pesan telah diperbarui")
# pesan.cetakIni()

