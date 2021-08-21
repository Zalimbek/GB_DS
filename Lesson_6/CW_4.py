class Unit:
    def __init__(self, name, hp, damage, armor, speed):
        self.name = name
        self.hp =hp
        self.armor = armor
        self.speed = speed
        self.damage= damage
    def attack(self, target):
        target_damage = self.damage - target.armor
        if target_damage >0:
            target.hp -= target.damage
            print(f'{self.name} атакует {target.name} с уроном {target_damage}')
        else:
            print(f'{self.name} проигрывает {target.name}')

    def run(self):
        print(f'{self.name} движется со скоростью {self.speed}')

class FlyUnitMixin:
    def fly(self, item):
        print(f'{self.name} используя {item} летит')

class Dragon(Unit, FlyUnitMixin):

    def __init__(self, name, hp, damage, armor, speed, fly_speed):
        Unit.__init__(self, name, hp, damage, armor, speed)
        self.fly_speed = fly_speed

    def fire_breath(self):
        print(f'{self.name} дышит огнем')

        # переопределение методов
    def attack(self, target):
        print('Дышим огнем')

class Witch(Unit, FlyUnitMixin):
    def witchcraft(self):
        print(f'{self.name} колдует')


orche = Unit('Орче', 100, 30, 20, 10)
knight = Unit('Рыцарь',80, 30, 30, 10)
gorinich =Dragon('Горыныч', 200, 50, 40, 20, 56)
yaga = Witch('Баба Яга',80, 30, 30, 10)


gorinich.attack()

# перегрузка
def func(a, b= None):
    if b:
        return a + b
    else:
        return a ** 2
# перегрузка
def func(a, b):
    if isinstance(b, int):
        return a + b
    else:
        return b * a


