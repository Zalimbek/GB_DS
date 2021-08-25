#Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.
# Решение через словарь:
seasons={"Зима": [12,1,2],
        "Весна": [3,4,5],
        "Лето": [6,7,8],
        "Осень": [9,10,11]}
print(seasons)
from_console=int(input('Введите число от 1 до 12: '))

print(from_console)
for season, month in seasons.items():
    if from_console in month:
        print(f'Выбранному числу соответствует сезон: {season}')

# Решение через список:
seasons=[["Зима", [12,1,2]],
        ["Весна", [3,4,5]],
        ["Лето", [6,7,8]],
        ["Осень", [9,10,11]]]
print(seasons)
from_console=int(input('Введите число от 1 до 12: '))

print(from_console)
for season, month in seasons:
    if from_console in month:
        print(f'Выбранному числу соответствует сезон: {season}')

