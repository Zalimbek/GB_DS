class Car:
    #атрибут класса
    auto_count = 0

    def create_car(self, name, speed):
        # атрибут объекта
        self.name = name
        self.speed = speed

    def start(self):
        print(f'{self.name} - двигатель заведен')


ferrari = Car()
zaz =Car()

ferrari.speed = 350
zaz.speed = 100
ferrari.doors =2
# ferrari.start()

print(zaz.auto_count, ferrari.auto_count)
print(ferrari.speed, zaz.speed)
print(ferrari.doors)

bmw = Car()
bmw.create_car('bmw', 200)
print(bmw.name, bmw.speed)
bmw.start()

