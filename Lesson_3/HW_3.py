# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def sum_of_2(a, b, c):
    try:
        new_list=[float(a),float(b),float(c)]
        max_1 = sorted(new_list)[2]
        max_2 = sorted(new_list)[1]
        result = max_1 + max_2
    except ValueError:
        return 'Ведите числовое значение!'
    return result

print(sum_of_2(input('Введите первое число: '),input('Введите второе число: '),input('Введите третье число: ')))