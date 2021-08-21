#  Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
#  В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
#  Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv

def salary():
    try:
        hours, salary_per_hour, bonus = map(float, argv[1:])
        total_salary = hours * salary_per_hour + bonus
    except ValueError:
        return ('Введите числовое значение!')
    print (f'Зарплата сотрудника: {total_salary}')

salary()
