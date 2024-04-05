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

    def apakahTerkandung(self, kata):
        if kata in self.teks.lower():
            return True
        else:
            return False

    def hitungKonsonan(self):
        length = self.jumKar()
        ans = 0
        for char in self.teks:
            if(char == 'a' or char == 'i' or char == 'u' or char == 'e' or char == 'o'):
                ans += 1;
            elif(char == 'A' or char == 'I' or char == 'U' or char == 'E' or char == 'O'):
                ans += 1;
        return length-ans

    def hitungVokal(self):
        ans = 0
        for char in self.teks:
            if(char == 'a' or char == 'i' or char == 'u' or char == 'e' or char == 'o'):
                ans += 1;
            elif(char == 'A' or char == 'I' or char == 'U' or char == 'E' or char == 'O'):
                ans += 1;
        return ans
