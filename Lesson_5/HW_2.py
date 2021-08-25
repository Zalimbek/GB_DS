# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

f = open('HW_1.txt', 'r', encoding='UTF-8')
line = 0
words_per_line = 0
for i in f:
    line += 1
    # print(i)
    words_per_line = len(i.split())
    print(f'Кол-во слов в строке {line}: {words_per_line}')
print(f'Число строк: {line}')
f.close()
