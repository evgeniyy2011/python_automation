from abc import ABC, abstractmethod

class Figura(ABC):

    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def perimetr(self):
        pass

class Romb(Figura):

    def __init__(self,rm_a:int,rm_h:int):
        """

        :param rm_a: сторона
        :param rm_h: висота
        """
        self.__rm_a = rm_a # сторона
        self.__rm_h = rm_h #висота

    def square(self): # розрахунок площі РОМБА
        squ_romb = self.__rm_a * self.__rm_h
        return squ_romb

    def perimetr(self): # розрахунок периметру РОМБА
        per = 4 * self.__rm_a
        return per

    def __str__(self):
        return f"Площа Ромба -{self.square()}\nПериметр Ромба - {self.perimetr()}\n{"-"*100}"

class Triangle(Figura):
    def __init__(self,tr_a:int, tr_b:int, tr_c:int, tr_h:int):
        """
        :param tr_a : основа / сторона A
        :param tr_b : сторона B
        :param tr_c : сторона C
        :param tr_h : высота, проведённая к стороне A
        """
        self.__tr_a = tr_a # основа/сторона А
        self.__tr_b = tr_b # сторона Б
        self.__tr_c = tr_c # сторона С
        self.__tr_h = tr_h # висота

    def square(self): # розрахунок площі ТРИКУТНИКА
        squ_triangle = (self.__tr_a * self.__tr_h) / 2
        return squ_triangle

    def perimetr(self): # розрахунок периметру ТРИКУТНИКА
        per = self.__tr_a + self.__tr_b + self.__tr_c
        return per


    def __str__(self):
        return f"Площа Трикутника -{self.square()}\nПериметр Трикутника - {self.perimetr()}\n{"-"*100}"

class Cube(Figura):
    def __init__(self, cb_a:int ):
        """
        :param cb_a : довжина однієї сторони
        """
        self.__cb_a = cb_a  # довжина однієї сторони

    def square(self): # розрахунок площі КУБА
        sue_cube = 6 * (self.__cb_a**2)
        return sue_cube

    def perimetr(self): # розрахунок периметру КУБА
        per = 12 * self.__cb_a
        return per

    def __str__(self):
        return f"{"-"*100}\nПлоща куба -{self.square()}\nПериметр куба - {self.perimetr()}\n{"-"*100}"

cub = Cube(4)
romb = Romb(5,8)
tr = Triangle(7,7,7,10)

for i in (cub,romb,tr):
    print(i)