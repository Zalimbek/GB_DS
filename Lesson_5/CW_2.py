# коретка, tell - позиция коретки

with open('secret.txt','r') as f:
    print(f.tell)
    print(f.read(20)) # прочитать 20 символов
    f.seek(0) # передвинуть указатель куда хотим

#----------------------------------------#
with open('data.txt','r') as f:
    print(f.tell())
    data = f.read()
    print(f.tell(), len(data))

#------------------------------#

with open('data.txt','w') as f:
    print('hahahha',file=f)



