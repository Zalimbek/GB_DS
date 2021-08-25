# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.

class IsNumber(Exception):

    def __str__(self):
        return 'Вы ввели не числовое значение. Веедите число!'

new_list = []

while True:
    from_console = input('Введите элемент списка или stop для выхода: ')
    if from_console.lower() == 'stop':
        break
    else:
        try:
            if not from_console.isdigit():
                raise IsNumber
            else:
                new_list.append(from_console)
        except IsNumber as e:
            print(e)


print(new_list)