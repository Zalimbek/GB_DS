# constructor
class Car:
    #атрибут класса
    auto_count = 0

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        Car.auto_count += 1


ferrari = Car('Феррари', 350)
ferrari.auto_count = 1000
print(ferrari.name, ferrari.speed, ferrari.auto_count)
zaz = Car('Запорожец', 100)
print(zaz.name, zaz.speed, zaz.auto_count)