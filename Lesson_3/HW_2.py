#Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def Person(**kwargs):
    return 'Person has the following information:'+', '.join(kwargs.values())


first_name = input('Введите имя: ')
last_name = input('Введите фамилию: ')
year_of_birth = input('Введите год рождения: ')
city = input('Введите город проживания: ')
email = input('Введите электронную почту: ')
phone = input('Ввведите телефон: ')

print(Person(first_name=first_name,last_name=last_name,year_of_birth=year_of_birth,city=city,email=email,phone=phone))




