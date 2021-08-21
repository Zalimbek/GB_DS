# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
# одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, name, size, height):
        self.name = name
        self.size = size
        self.height = height

    @property
    @abstractmethod
    def material_amount(self):
        pass

    def __add__(self, other):
        return self.material_amount + other.material_amount

class Suit(Clothes):
    def __init__(self, name, height, size=0):
        Clothes.__init__(self, name, size, height)

    @property
    def material_amount(self):
        return 2 * self.height + 0.3

class Coat(Clothes):
    def __init__(self, name, size, height=0):
        Clothes.__init__(self, name, size, height)


    @property
    def material_amount(self):
        return self.size / 6.5 + 0.5


coat = Coat("Зимнее пальто", 42)
suit = Suit("Офисный костюм", 12)
print(round(coat + suit))

