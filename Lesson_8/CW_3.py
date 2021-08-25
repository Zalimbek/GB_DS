def division(a, b):
    res = a / b
    return res
try:
    print(division(10, 0))

except Exception as e:
    print(f'Ошибка! - {e}')

except (ZeroDivisionError, TypeError):
    print('Делить на ноль нельзя')

print('Конец программы')