time_in_sec = int(input('Введите время в секундах: '))
hours = time_in_sec//3600
minutes = time_in_sec//60 - hours * 60
seconds = time_in_sec % 60
print(f'Введенное время: {hours:02}:{minutes:02}:{seconds:02}')