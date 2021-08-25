# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

class Storage():
    pass

class Devices:

    def __init__(self, name, brand, model, color, price, can_print=False, can_scan=False):
        self.name = name
        self. brand = brand
        self.model =  model
        self.color = color
        self.price = price

    def __str__(self):
        return f'{self.color} {self.name} : производитель - {self.brand} , модель - {self.model}, цена - {self.price}'

class Printer(Devices):
    def __init__(self, name, brand, model, color, price, can_print=True, can_scan=False):
        super().__init__(name, brand, model, color, price)
        # can_print = True
        # can_scan = False

class Scaner(Devices):
    def __init__(self, name, brand, model, color, price, can_print=False, can_scan=True):
        super().__init__(name, brand, model, color, price)
        # can_print = False
        # can_scan = True

class Xerox(Devices):
    def __init__(self, name, brand, model, color, price, can_print=True, can_scan=True):
        super().__init__(name, brand, model, color, price)
        # can_print = True
        # can_scan = True

xerox = Xerox('ксерокс', 'Epson', 'EP120','черный', 1200)
print(xerox)