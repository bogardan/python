'''
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
'''

import random

class Matrix:
    def __init__(self,line: int, column: int):
        self.line = line
        self.column = column
        self.matrix = [[random.randint(0, 10) for x in range(self.line)] for y in range(self.column)]

    def __str__(self):
        matrix = self.matrix
        for itm in range(len(matrix)):
            print(matrix[itm])

    def __add__(self, other):
        res = Matrix(self.line,self.column)
        res.matrix =[]
        for x in range(len(self.matrix)):
            temp = []
            for y in range(len(self.matrix[x])):
                z = self.matrix[x][y] + other.matrix[x][y]
                temp.append(z)
            res.matrix.append(temp)
        return res

# mat1 = Matrix(2,2)
# mat2 = Matrix(2,2)

print(1)
