income = float(input('Введите значение выручки: '))
spent = float(input('Введите значение издержек: '))

dif = income - spent

if dif > 0:
    print(f'Прибыль фирмы {income}. Рентабельность фирмы: {dif / income}')
    employees = int(input('Введите число сотрудников: '))
    print(f'Прибыль фирмы на одного сотрудника: {dif / employees}')

else:
    print(f'Убыток фирмы {spent}.')