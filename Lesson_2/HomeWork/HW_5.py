# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]

from_console=int(input("Введите целое число: "))

frequency = my_list.count(from_console)
print(frequency)

for i in my_list:
    # Если число уже есть в списке
    if frequency>0:
        index_end=my_list.index(from_console)
        my_list.insert(index_end+frequency,from_console)
        break
    else:
    # Если число больше максимального из списка
        if from_console>i:
            index_begin=my_list.index(i)
            my_list.insert(index_begin,from_console)
            break
        else:
    # Если число меньше минимального из списка
            if from_console<my_list[len(my_list)-1]:
                my_list.append(from_console)

print(my_list)