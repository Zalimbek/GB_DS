number = int(input('Введите положительное целое число: '))
i = number
maximum = number % 10

while i > 0:
    digit = i % 10
    if digit == 9:
        break

    if digit > maximum:
        maximum = digit

    i = i // 10
    print(i)

print(f'Наибольшее число {maximum}')
