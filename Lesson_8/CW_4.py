def div(*args):
    for i in args:
        try:
            print(10 / i)
        except ZeroDivisionError:
            print('На ноль делить нельзя')
    print('Функция div завершилась')


def main():
    div(10, 20, 100, 0, 50)
    print('Функция main завершилась')

# try:
main()
# except Exception as e:
#     print(e)
print('Программа завершилась')