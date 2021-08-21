# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и т.д.

a = [[1,2,3], [1,2,3], [1,2,3]]
b = [[3,2,1], [3,2,1], [3,2,1]]

class Matrix:
    def __init__(self,list_of_lists):
        self.list_of_lists = list_of_lists

    def __str__(self):
        return '\n'.join(map(str, self.list_of_lists))

    def __add__(self, other):
        sum_of_matx = []
        for i in range(len(self.list_of_lists)):
            sum_of_matx.append([])
            for j in range(len(self.list_of_lists[0])):
                sum_of_matx[i].append(self.list_of_lists[i][j] + other.list_of_lists[i][j])
            return '\n'.join(map(str, sum_of_matx))


mat1 = Matrix(a)
mat2 = Matrix(b)

print(f'Matrix 1:\n{mat1}\n')
print(f'Matrix 2:\n{mat2}\n')
print(f'Сумма двух матриц: {mat1 + mat2}')

