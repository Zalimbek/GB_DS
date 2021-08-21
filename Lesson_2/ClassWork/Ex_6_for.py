data=['Hello',123, 84.6]

i=0

# while i< len(data)
#     print(data[i])
#     i+=1

for i in data:
    print(i)

for num, element in enumerate(data):
    print(num, element)

#тернарный опрератор
# Ex1
is_checked=True
mode="checked" if is_checked else "not checked"
print(mode)
#Ex2
checked=True
personality=("Проверено", "Не проверено") [checked]
print(personality)
#Ex3

print(True or "Some")
print(False or "Some")
#Ex4
func_return = None
message = func_return or "Функция ничего не возвращает"
print(message)