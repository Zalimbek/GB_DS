# # modules os, json, shutil
# #os работа с операционной системой
#
# import os
#
# os.remove('secret.txt') # удаляет файл
# os.rename('secret.txt','akakak.pdf') # переименовывает файл
# print(os. listdir()) # список всех файлов в директори
#
# #-------------------#
#
# #isdir -является ли директорией
# #isfile - является ли файдом
#
# from os.path import isdir, isfile
#
# for el in os.listdir():
#     if isfile(el):
#         print(el)
#
# # shutil - для работы с файлами
# import shutil
#
# with open('data_write.txt','r') as fr, open('data_r.txt', 'a') as fa:
#     shutil.copyfileobj(fr, fa)
#
# shutil.
#
# # sys

import sys
print(sys.executable)

print(sys.path) # ищет библиотеки, подключены ли
print(sys.platform) #darwin, posix, win32 - интерфейс общения с ОС

#json

import json

# with open('data.json', 'r') as f:
#     data = json.load(f)
# print(data)

data={
    'name':'Steve',
    'age': 23
}
with open('person.json', 'w') as f:
    json.dump(data,f)
print(data)
