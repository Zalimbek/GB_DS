# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и
# не завершиться с ошибкой.

class DivZero(Exception):

    def __str__(self):
        return 'Делить на ноль нельзя'

class Number(float):
    def __truediv__(self, other):
        if other == 0:
            raise DivZero
        else:
            return float(self) / float(other)


try:
     div1 = Number(input('Введите делимое: '))
     div2 = Number(input('Введите делитель: '))
     print(div1 / div2)
except (DivZero, ValueError) as e:
     print(e)
