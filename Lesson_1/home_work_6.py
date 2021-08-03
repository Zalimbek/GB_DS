a_km = float(input('Введите результат за первый день в км: '))
b_km = float(input('Введите желаемый результат в км: '))
day = 1

result = a_km

while result < b_km:
    result = 1.1 * result
    day = day + 1

print(f'На {day}-й день спортсмен достиг резултата - не менее {b_km} км')