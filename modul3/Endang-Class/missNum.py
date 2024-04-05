class NumList:
    def __init__(self, num) -> None:
        if isinstance(num, list):
            self.data = num
        elif '[]' in num:
            num = num.replace("[", "").replace("]", "")
            num = num.split(', ') if ', ' in num else num.split(',') if ',' else num
            for i in range(0, len(num)):
                num[i] = int(num[i])
            self.data = num
        elif ',' in num:
            num = num.split(', ') if ', ' in num else num.split(',') if ',' else num
            for i in range(0, len(num)):
                num[i] = int(num[i])
            self.data = num
        else:
            self.data = None
            print('Input are not "list" type data')

    def findMiss(self) -> None:
        lnum = self.data
        for i in range(0, len(lnum)):
            if i == 0:
                continue
            if lnum[i]-1 != lnum[i-1]:
                print('\nMissing number is', lnum[i]-1)
                break

def main():
    num = NumList(input('Input :'))
    num.findMiss()

if __name__ == '__main__':
    main()