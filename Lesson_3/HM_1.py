# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def DIV(a , b):
    try:
        result = float(a) / float(b)
    except ValueError:
        return 'Введите числовое значение!'
    except ZeroDivisionError:
        return "Делить на ноль нельзя!"
    return result

number_1 = input('Введите первое число: ')
number_2 = input('Введите второе число: ')
print(DIV(number_1, number_2))