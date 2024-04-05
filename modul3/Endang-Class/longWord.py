class Teks:
    def __init__(self, text):
        self.data = text

    def list_kata(self):
        ans = self.data.split()
        return ans
    
    def panjang(self):
        kata = self.list_kata()
        lword = kata[0]
        for x in kata:
            if len(x) > len(lword):
                lword = x
        print('\nthe longest word is', lword)

def main():
    text = Teks(input("Input: "))
    text.panjang()

if __name__ == '__main__':
    main()
