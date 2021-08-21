#Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

rus_numbers = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("HW_4_rus.txt",'w', encoding='UTF-8') as rus:
    with open("HW_4.txt",'r', encoding='UTF-8') as en:
        for i in en:
            rus.write(str(i.replace(i.split()[0],rus_numbers.get(i.split()[0]))))
