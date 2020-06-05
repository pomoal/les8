# Практическое задание
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.
#
import random

my_list = []
my_matrix2= []

matrix_size = [random.randint(2,5), random.randint(2,5)]
# print(matrix_size)

def matrix_generation(size):
    my_temp_list = []
    for el in range(size[0]):
        temp_list = []
        for el in range(size[1]):
            temp_list.append(random.randint(1, 25))
        my_temp_list.append(temp_list)
    return my_temp_list

my_list = matrix_generation(matrix_size)
my_matrix2 = matrix_generation(matrix_size)

class Matrix():
    def __init__(self, matr_list=None):
        self.matrix = matr_list
        self.size = [len(matr_list),len(matr_list[0])]

    def __str__(self):
        super.__str__(self)
        temp_list = []
        max_lengt = 0
        for el in range(len(self.matrix)):
            for el2 in self.matrix[el]:
                if max_lengt<=len(str(el2)): max_lengt = len(str(el2))
        for el in range(len(self.matrix)):
            temp = ""
            str_space = ""
            for el2 in self.matrix[el]:
                if len(str(el2))<max_lengt: str_space = " "
                else: str_space =""
                temp += str_space + str(el2) + " "
            temp += " \n"
            temp_list.append(''.join(temp))
        return ''.join(temp_list)

    def __add__(self, other):
        if self.size == other.size:
            for el in range(self.size[0]):
                temp_list =list(self.matrix[el])
                temp_list2=list(other.matrix[el])
                for el2 in range(len(temp_list)):
                    temp_list[el2] += temp_list2[el2]
                self.matrix[el] = temp_list
        else:
            print('Матрицы разного размеры, нельзя складывать!')
        return self

my_matrix = Matrix(my_list)
my_matrix2 = Matrix(my_matrix2)
print(my_matrix)
print(my_matrix2)
print(my_matrix + my_matrix2)

