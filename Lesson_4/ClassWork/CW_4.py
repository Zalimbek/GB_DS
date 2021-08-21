## модули

## random

from random import randint, randrange,random,choice

# print(randint(1,10)) #правая часть включается
# print(randrange(10)) #генерирует от 0 до 9, может включать шаг
# print(random()) # float от 0 до 1, 1 не включается

a=[100,'Hello',99.5]
print(choice(a))

## functools
# count создает итератор с указанного числа, с шагом 1 по дефолту
# cycle повторяет список, если дошел до конца

from functools import reduce
from itertools import count, cycle

def f(a,b):
    return a+b

print(reduce(f,[10,20,30,40])) #складывает последовательно
# счетчик
for i in count(10):
    if i==51:
        break
    print(i)

#счетчик, который перебирает последовательность
count=0
for i in cycle(['A','B','C']):
    if count==11:
        break
    count+=1
    print(i)


