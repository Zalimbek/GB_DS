#Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationary:
    def __init__(self, title):
        self.title = title

    def Draw(self):
        print(f'{self.title}:\n Запуск отрисовки')

class Pen(Stationary):
    def Draw(self):
        print(f'{self.title}:\nЗапуск отрисовки ручкой')
class Pencil(Stationary):
    def Draw(self):
        print(f'{self.title}:\nЗапуск отрисовки карандашом')

class Handle(Stationary):
    def Draw(self):
        print(f'{self.title}:\nЗапуск отрисовки маркером')

pen = Pen('Я рисую ручкой')
pen.Draw()

pencil = Pencil('Я рисую карадашом')
pencil.Draw()

handle = Handle('Я рисую маркером')
handle.Draw()

stationary = Stationary('Здесь будет зарисовка')
stationary.Draw()


