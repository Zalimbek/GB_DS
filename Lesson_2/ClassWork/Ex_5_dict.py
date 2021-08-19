person={'name': 'Tom','age': 43}

print(person['name'])

person['car']='ferrari'
print(person)
print(list(person.values()))
print(list(person.keys()))
print(person.get('home', 'Поле не найдено')) #такого ключа нет, выдает none -защищает от ошибки
print(person.get('age', 'Поле не найдено')) #если такого нет, то , выдает сообщение после запятой -защищает от ошибки, иначе выдает верный ответ

key=input('Введите значение ключа: ') #add key and new value
value=input('Введите значение: ')
person[key]=value
print(person)

# example with list of dicts
data=[
    {
        'name': 'Tom',
        'age': 43,
        'cars': ['ferrari', 'zaporojetz']
    },
    {
        'name': 'Steve',
        'age': 57
    }
]
print(data[0]['cars'][0])

#Сортировка словаря по значениям
my_dict = {'python': 1991, 'java': 1995, 'c++': 1983}
print(sorted(my_dict))