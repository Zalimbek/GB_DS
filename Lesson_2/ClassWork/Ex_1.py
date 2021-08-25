# a='Hello World!'
# print(a[-1])
# print(a[::-1])
# print(a.upper())
# print(a.find('orl'))
# print(a.count('Wo'))
# print(a.replace('ll','zzz'))
#
# num=int(input('введите число- '))
# if a.isdigest():
#     num=int(int)
# else:
#     print('Incorrect data')

## lists
data=['Hello', 34.7, 12, True]
print(data[2:3])
data[0]='Hi'
print(data)
data.append('Hey')
print(data)

data.insert(1,'low')
print(data)
a=data.pop(1) #забирает последний элемент () и конкретный если в скобках число
print(a)

c=[1,2,3]
data.extend(c)
print(data) # склеивает списки

