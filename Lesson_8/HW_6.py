# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.
class NotAnItem(Exception):

    def __str__(self):
        return 'Предмет не относится к оргтехнике!'

class Storage():
    def __init__(self):
        self.storage = {'Ксерокс': 0, 'Принтер': 0, 'Сканер': 0}
        self.list = []
    def add_item(self, item):
        try:
            if isinstance(item, Xerox):

                self.list.append('Ксерокс')
                self.storage['Ксерокс'] = self.list.count('Ксерокс')
            elif isinstance(item, Scaner):

                self.list.append('Сканер')
                self.storage['Сканер'] = self.list.count('Сканер')
            elif isinstance(item, Printer):

                self.list.append('Принтер')
                self.storage['Принтер'] = self.list.count('Принтер')
            else:
                raise NotAnItem
        except NotAnItem as e:
            print(item, e)

    def del_item(self, item):
        try:
            if isinstance(item, Xerox):

                self.list.remove('Ксерокс')
                self.storage['Ксерокс'] = self.list.count('Ксерокс')
            elif isinstance(item, Scaner):

                self.list.remove('Сканер')
                self.storage['Сканер'] = self.list.count('Сканер')
            elif isinstance(item, Printer):

                self.list.remove('Принтер')
                self.storage['Принтер'] = self.list.count('Принтер')
            else:
                raise NotAnItem
        except NotAnItem as e:
            print(item, e)

    def move(self, item, department):
        print(f'{item} передан в департамент: {department}')


    def __str__(self):
        return f'На складе сейчас: {self.storage}'
class Devices:

    def __init__(self, name, brand, model, color, price, can_print=False, can_scan=False):
        self.name = name
        self. brand = brand
        self.model = model
        self.color = color
        self.price = price

    def __str__(self):
        return f'{self.color} {self.name} : производитель - {self.brand} , модель - {self.model}, цена - {self.price}'


class Printer(Devices):
    def __init__(self, name, brand, model, color, price, can_print=True, can_scan=False):
        super().__init__(name, brand, model, color, price)
        can_print = True
        can_scan = False

class Scaner(Devices):
    def __init__(self, name, brand, model, color, price, can_print=False, can_scan=True):
        super().__init__(name, brand, model, color, price)
        can_print = False
        can_scan = True

class Xerox(Devices):
    def __init__(self, name, brand, model, color, price, can_print=True, can_scan=True):
        super().__init__(name, brand, model, color, price)
        can_print = True
        can_scan = True

xerox = Xerox('ксерокс', 'Epson', 'EP120','черный',  200)
printer = Printer('Принтер', 'LG', 'EP120','черный', 2000)
scaner = Scaner('Сканер', 'HP', 'EP120','черный', 1000)
xerox_new = Xerox('ксерокс', 'Philips', 'EP120','черный', 1400)
storage = Storage()
storage.add_item(xerox)
storage.add_item(xerox_new)
storage.add_item(scaner)
storage.add_item(printer)

storage.move(xerox, 'Бухгалтерия')
storage.move(xerox_new, 'Безопасность')
storage.move(printer,'Отдел кадров')

storage.del_item(xerox)
storage.del_item(xerox_new)
storage.del_item(printer)

print(storage)