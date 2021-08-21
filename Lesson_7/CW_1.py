class Auto:
    def __init__(self, name,speed):
        self.name = name
        self.speed = speed

    def __str__(self): #отвечает за то, что будет выводиться print(ferrari)
        return self.name

    def __add__(self, other):# как ведете себя объект при сложении
        #return f'{self.name} столкнулся с {other.name}'
        return Auto(self.name + other.name, self.speed + other.speed)

    def __radd__(self, other):# если объект стоит справа, вызовется для zaz
        pass

    def __iadd__(self, other):# для zaz += 1
        pass

    def __getitem__(self, item):
        return item ** 2

    def __setattr__(self, key, value): #zaz.doors =4, doors -key, 4 - value
        if key =='speed' and value > 430:
            print('Это не самолет, скорость установлена 430')
            self.__dict__['speed'] = 430
        else:
            self.__dict__[key] = value

    def __eq__(self, other):
        return self.speed == other.speed


ferrari =Auto('Феррари', 350)
zaz = Auto('Запорожец', 90)
zaz.speed = 780
# zaz.doors = 2
# zaz.__dict__['doors'] = 2

print(zaz.speed)
print(zaz == ferrari)
# uaz = Auto('УАЗ', 180 )
#
# print(ferrari + zaz + uaz)

