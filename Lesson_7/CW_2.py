class Auto:
    def __init__(self, name, speed):
        self.name = name
        self.speed =speed
        self.year = 2017

    def __fuel_pump(self):# __fuel_pump это private, _ - protected
        print('качаем топливо')

    def start(self):
        self.__fuel_pump()
        print('Заводим двигатель')

ferrari =Auto('Феррари', 350)
# ferrari.fuel_pump()
ferrari.start()

