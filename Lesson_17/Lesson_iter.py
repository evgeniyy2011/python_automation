class Iterator:
    def __init__(self, spisok:list):
        self.__spisok = spisok
        self.index = len(self.__spisok)-1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index<0:
            raise StopIteration
        res = self.__spisok[self.index]
        self.index -=1
        return res

numb = Iterator([1,2,3,4,5,6,7,8,9])
for i in numb:
    print(i)
