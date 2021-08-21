# Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randint
with open('HW_5.txt','w+', encoding='UTF-8') as f:
    for i in range(100):
        f.write(" ".join(str(randint(1, 100))))
        f.seek(0)
        print(sum(map(int,f.readline().split())))
