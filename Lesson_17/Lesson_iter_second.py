
class Even:

    def __init__(self, n:int):
        self.__n = n
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter > self.__n:
            raise StopIteration
        answer = self.counter
        self.counter+=2
        return answer

res = Even(20)
for i in res:
    print(i)