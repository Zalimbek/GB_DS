f = open('data.txt','r')
data = f.read()
print(data)
f.close()

#--------------------#
f = open('data.txt','r')
print(f.readlines()) # считывает значения и возвращает как список
#-----------------------#
# w - если файл существует, он перезаписывает. Если файл не существует, он создает с нуля
# x не позволяет пересоздавать файл
# a add- добавить что то в файл
# w+, a+, r+ читать и писать одновременно
# rb, wb -работа с бинарными файлами
f = open('secret.txt', 'w')
print(f.write('TOP-SECRET-PASSWORD-qwerty123'))
f.close()

# менеджер контекста
with open('secret.txt','w') as f:
    print(f.write('chhghjhg'))
# flush - сохранить без закрытия файла

# name - имя файла
# closed - закрыт ли файл в данный момент
# mode - в каком режиме был открыт
with open('secret.txt', 'r') as f:
    print(f.name)
    print(f.closed)
    print(f.mode)