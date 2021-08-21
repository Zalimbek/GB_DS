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

class Dragon(Unit):
    def fire_breath(self):
        print(f'{self.name} дышит огнем')
    def fly(self):
        print(f'{self.name} летит')

class Witch(Unit):
    def witchcraft(self):
        print(f'{self.name} колдует')

    def fly(self):
        print(f'{self.name} летит на метле')

class WitchDragon(Witch, Dragon):
    def who_am_i(self):
        print('Что это такое??')

orche = Unit('Орче', 100, 30, 20, 10)
knight = Unit('Рыцарь',80, 30, 30, 10)
gorinich =Dragon('Горыныч', 200, 50, 40, 20)
yaga = Witch('Баба Яга',80, 30, 30, 10)
chudo_yudo = WitchDragon('Чудо-Юдо', 200, 50, 40, 20)
chudo_yudo.fly()

yaga.attack(gorinich)
yaga.fly()
yaga.witchcraft()
gorinich.fire_breath()
gorinich.run()

gorinich.attack(knight)
print(knight.hp)