import numpy as np


class HashMixin:
    def __hash__(self):
        # Простейшая хэш-функция.
        # Мы берем сумму всех элементов, умножаем на количество строк и столбцов.
        return hash(self.data.sum() * self.rows * self.cols)


class Matrix(HashMixin):
    def __init__(self, data):
        self.data = np.array(data)
        self.rows, self.cols = self.data.shape
        self._cache = None

    def __repr__(self):
        return f"Matrix({self.data})"

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition")
        return Matrix(self.data + other.data)

    def __mul__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for element-wise multiplication")
        return Matrix(self.data * other.data)

    def __matmul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Matrices must have compatible dimensions for matrix multiplication")

        if self._cache is not None:
            return self._cache

        result = Matrix(np.dot(self.data, other.data))

        self._cache = result

        return result

    def clear_cache(self):
        self._cache = None


np.random.seed(0)
matrix_a = Matrix(np.random.randint(0, 10, (10, 10)))
matrix_b = Matrix(np.random.randint(0, 10, (10, 10)))

matrix_sum = matrix_a + matrix_b
matrix_elementwise_multiply = matrix_a * matrix_b
matrix_matrix_multiply = matrix_a @ matrix_b

with open("hw_3/artifacts/matrix+.txt", "w") as f:
    f.write(str(matrix_sum.data))

with open("hw_3/artifacts/matrix*.txt", "w") as f:
    f.write(str(matrix_elementwise_multiply.data))

with open("hw_3/artifacts/matrix@.txt", "w") as f:
    f.write(str(matrix_matrix_multiply.data))

np.random.seed(0)
A = Matrix(np.random.randint(0, 10, (10, 10)))
B = Matrix(np.random.randint(0, 10, (10, 10)))

# Мы создадим матрицу C, которая будет иметь тот же хэш, что и A, но отличаться по содержимому.
C = Matrix(A.data.copy())
C.data[0, 0] = 99  # Сделаем A и C разными, изменив только один элемент.

# Матрица D будет идентична B.
D = Matrix(B.data.copy())

with open("hw_3/artifacts/A.txt", "w") as f:
    f.write(str(A.data))

with open("hw_3/artifacts/B.txt", "w") as f:
    f.write(str(B.data))

with open("hw_3/artifacts/C.txt", "w") as f:
    f.write(str(C.data))

with open("hw_3/artifacts/D.txt", "w") as f:
    f.write(str(D.data))

AB = A @ B
CD = C @ D

with open("hw_3/artifacts/AB.txt", "w") as f:
    f.write(str(AB.data))

with open("hw_3/artifacts/CD.txt", "w") as f:
    f.write(str(CD.data))

with open("hw_3/artifacts/hash.txt", "w") as f:
    f.write(f"hash(A) == hash(C): {hash(A) == hash(C)}\n")
    f.write(f"hash(B) == hash(D): {hash(B) == hash(D)}\n")
    f.write(f"hash(A) == hash(C): {hash(A)} == {hash(C)}\n")
    f.write(f"hash(B) == hash(D): {hash(B)} == {hash(D)}\n")

A.clear_cache()
C.clear_cache()
