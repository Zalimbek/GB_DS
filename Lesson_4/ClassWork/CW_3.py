# def gener():
#     for i in (1,2,3):
#         yield i
#         print('перезарядка')
#
# g=gener()
#
# print(next(g))
# # print(next(g))
#
# for i in g:
#     print(i)

def my_range(start,end,step=1):
    while start<end:
        yield start
        start+=step

a=my_range(0,5)
for i in a:
    print(i)

data=(el for el in range(0,11))
## запись выше аналогична записи ниже-компрехеншн для генератора
def gen():
    for i in range(0,11):
        yield  el
print(data)