class Auto:
    name = 1

    def __init__(self, name):
        self.name = name

    @staticmethod
    def info():
        print('Я автомобиль')

    @classmethod
    def change_name(cls):
        cls.count += 1

Auto.info()

class A(Auto):
    pass

A.change_name()


