# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class ComplexNumber:
    def __init__(self, real, image):
        self.real = real
        self.image = image
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'z = {self.real + other.real} + {self.image + other.image} * i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'z = {self.real * other.real - (self.image * other.image)} + {self.image * other.real} * i'

    def __str__(self):
        return f'z = {self.real} + {self.image} * i'


z_1 = ComplexNumber(1, 1)
z_2 = ComplexNumber(-4, -3)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)