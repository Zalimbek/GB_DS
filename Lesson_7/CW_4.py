data = [10, 20, 'Hello']

class Iterator:
    def __init__(self, start, stop):
        self.start =start-1
        self.stop = stop

    def __next__(self):
        self.start += 1
        while True:
            if self.start < self.stop:
                return self.start
            else:
                raise StopIteration

    def __iter__(self):
        return self

# class IterObj:
#     def __init__(self, start, stop):
#         self.start =start
#         self.stop = stop
#
#     def __iter__(self):
#         return Iterator(self.start, self.stop)

iter_obj = Iterator(0, 10)
for i in iter_obj:
    print(i)
# data_iter = data.__iter__()
# while True:
#     try:
#         print(next(data_iter))
#     except StopIteration:
#         break
#
# for i in data:
#     print(i)