#Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

from_console = input("Введите значения через запятую: ")
new_list = from_console.split(',')
print(new_list)
print(type(new_list))

for i in range(1, len(new_list), 2):
    tmp = new_list[i-1]
    new_list[i-1] = new_list[i]
    new_list[i] = tmp


print(new_list)