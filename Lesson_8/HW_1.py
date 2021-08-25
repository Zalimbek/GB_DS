# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать
# их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:

    def __init__(self, date):
        self.date = date

    @classmethod
    def data_extract(cls, date):
        if not date.__contains__("-"):
            return 'Введите дату в формате 00-00-0000'
        else:
            day, month, year = map(int, date.split("-"))
            return f'День: {day}, Месяц: {month}, Год: {year}'

    @staticmethod
    def date_validation(date):
        if not date.__contains__("-"):
            return 'Введите дату в формате 00-00-0000'
        else:
            day, month, year = map(int, date.split("-"))
        if 0 > day > 32:
            return 'Даты могут быть в пределах 1..31'
        if 0 > month > 13:
            return 'Месяца могут быть от 1 до 12'
        else:
            return 'Даты введены верно'

new_date = Data("12-12-2012")
print(new_date.date)
print(Data.data_extract("12-12-2012"))
print(Data.date_validation("12-12-2012"))

