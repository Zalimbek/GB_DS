class Auto:

    def __init__(self, cost, s):
        self.cost = cost
        self.s =s

    @property
    def real_coast(self):
        return self.cost -self.s*2

uaz =Auto(800_000, 90000)
print(uaz.real_coast)

@dataclass

class Person:
    name: str
    age: int