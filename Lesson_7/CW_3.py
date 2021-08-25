from abc import ABC, abstractmethod

class Boss(ABC):

    @abstractmethod
    def a(self):
        pass

    @abstractmethod
    def b(self):
        pass

class Worker(Boss):

    def work(self):
        print('Я работаю!')

    def a(self):
        print('Метод а')
    def b(self):
        print('Метод b')

tom = Worker()
tom.work()