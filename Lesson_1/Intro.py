true_password = '1234'
number_of_attempts = 3

user_password = input('Введите пароль - ')

while True:

    if user_password == true_password:
        print('Доступ разрешен')
        break

    else:
        number_of_attempts = number_of_attempts - 1

        if number_of_attempts == 0:
            print('Все попытки исчерпаны. Доступ запрещен!')
            break

        print(f'Неверный пароль! Повторите ввод\nОсталось попыток {number_of_attempts}')
        user_password = input('Введите пароль - ')
