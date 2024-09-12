# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

from_console = input("Введите строку из нескольких слов: ")
print(from_console)
new_list = from_console.split()

for num, element in enumerate(new_list):
    if len(new_list[num])<10:
        print(num,element)
    else: print(num,element[:10])
