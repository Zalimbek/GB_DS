#Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} начала движение')

    def stop(self):
        print(f'Машина {self.name} прекратила движение')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Скорость {self.name}: {self.speed}')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Машина {self.name} превысила скорость на {self.speed -60}')
        else:
            print(f'Скорость {self.name}: {self.speed}')

class SportCar(Car):
    """fdffdfd"""

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'Машина {self.name} превысила скорость на {self.speed -40}')
        else:
            print(f'Скорость {self.name}: {self.speed}')

class PoliceCar(Car):
    def __init__(self, name, speed, color, is_police=True):
        Car.__init__(self, name, speed, color)
        is_police = True


police_car = PoliceCar('Rosgvardia', 100, 'Black')
police_car.go()
police_car.turn('Налево')

town_car = TownCar('Oka', 100, 'White')
town_car.stop()
town_car.show_speed()

work_car = WorkCar('Gazel', 100, 'Blue')
work_car.show_speed()
work_car.go()

sport_car = SportCar('Ferrari', 200, 'Red')
sport_car.show_speed()
sport_car.stop()


