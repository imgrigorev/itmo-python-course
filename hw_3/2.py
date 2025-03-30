# import numpy as np
#
#
# class MatrixOperations:
#     def __add__(self, other):
#         if self.rows != other.rows or self.cols != other.cols:
#             raise ValueError("Matrices must have the same dimensions for addition")
#         return Matrix(self.data + other.data)
#
#     def __sub__(self, other):
#         if self.rows != other.rows or self.cols != other.cols:
#             raise ValueError("Matrices must have the same dimensions for subtraction")
#         return Matrix(self.data - other.data)
#
#     def __mul__(self, other):
#         if self.rows != other.rows or self.cols != other.cols:
#             raise ValueError("Matrices must have the same dimensions for element-wise multiplication")
#         return Matrix(self.data * other.data)
#
#     def __truediv__(self, other):
#         if self.rows != other.rows or self.cols != other.cols:
#             raise ValueError("Matrices must have the same dimensions for element-wise division")
#         return Matrix(self.data / other.data)
#
#     def __matmul__(self, other):
#         if self.cols != other.rows:
#             raise ValueError("Matrices must have compatible dimensions for matrix multiplication")
#         return Matrix(np.dot(self.data, other.data))
#
#     def __repr__(self):
#         return f"Matrix({self.data})"
#
#
# class Matrix(MatrixOperations):
#     def __init__(self, data):
#         self._data = np.array(data)
#         self._rows, self._cols = self._data.shape
#
#     @property
#     def data(self):
#         return self._data
#
#     @data.setter
#     def data(self, value):
#         self._data = np.array(value)
#         self._rows, self._cols = self._data.shape
#
#     @property
#     def rows(self):
#         return self._rows
#
#     @property
#     def cols(self):
#         return self._cols
#
#     def __str__(self):
#         return f"Matrix({self._data})"
#
#     def save_to_file(self, filename):
#         np.savetxt(filename, self._data, fmt="%d")
#
#     @classmethod
#     def from_file(cls, filename):
#         data = np.loadtxt(filename, dtype=int)
#         return cls(data)
#
#
# # Генерация двух матриц размером 10x10 с целыми числами от 0 до 9
# np.random.seed(0)
# matrix_a = Matrix(np.random.randint(0, 10, (10, 10)))
# matrix_b = Matrix(np.random.randint(0, 10, (10, 10)))
#
# # Операции над матрицами
# matrix_sum = matrix_a + matrix_b
# matrix_difference = matrix_a - matrix_b
# matrix_elementwise_multiply = matrix_a * matrix_b
# matrix_elementwise_divide = matrix_a / matrix_b
# matrix_matrix_multiply = matrix_a @ matrix_b
#
# # Запись результатов в файлы
# matrix_sum.save_to_file("matrix+.txt")
# matrix_difference.save_to_file("matrix-.txt")
# matrix_elementwise_multiply.save_to_file("matrix*.txt")
# matrix_elementwise_divide.save_to_file("matrix/.txt")
# matrix_matrix_multiply.save_to_file("matrix@.txt")
#
# # Вывод в консоль
# print(matrix_sum)
# print(matrix_difference)
# print(matrix_elementwise_multiply)
# print(matrix_elementwise_divide)
# print(matrix_matrix_multiply)
#
# # Чтение матрицы из файла
# loaded_matrix = Matrix.from_file("matrix+.txt")
# print(loaded_matrix)

import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin


class FileWriteMixin:
    def write(self, file_path):
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(str(self.data) + '\n\n')


class StrMixin:
    def __str__(self):
        return f'{self.data}'


class Descriptor:
    def __get__(self, instance, owner):
        return instance.__dict__['_data']

    def __set__(self, instance, value):
        instance.__dict__['_data'] = value


class DescriptorMixin:
    data = Descriptor()


class ArrayWrapper(NDArrayOperatorsMixin, StrMixin, FileWriteMixin, DescriptorMixin):
    def __init__(self, data):
        self._data = np.array(data)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        args = [x.data if isinstance(x, ArrayWrapper) else x for x in inputs]
        result = getattr(ufunc, method)(*args, **kwargs)

        if isinstance(result, np.ndarray):
            return ArrayWrapper(result)
        return result


a = ArrayWrapper([[1, 2, 3], [4, 5, 6]])
a.write('hw_3/artifacts/mixins_artifacts.txt')
b = ArrayWrapper([[1, 3, 5], [7, 9, 11]])
b.write('hw_3/artifacts/mixins_artifacts.txt')
c = a + b
c.write('hw_3/artifacts/mixins_artifacts.txt')
d = 2 * c
d.write('hw_3/artifacts/mixins_artifacts.txt')
e = d * c
e.write('hw_3/artifacts/mixins_artifacts.txt')
