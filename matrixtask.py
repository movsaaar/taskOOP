import random

class Matrix:
    def __init__(self, rows, cols, min_val=0, max_val=9, data=None):
        self.rows = rows
        self.cols = cols
        if data:
            self.data = data
        else:
            self.data = [
                [random.randint(min_val, max_val) for _ in range(cols)]
                for _ in range(rows)
            ]

    def __repr__(self):
        return "\n".join(["\t".join(map(str, row)) for row in self.data])

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        return self.data == other.data

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны быть одного размера")
        result_data = [
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(self.rows, self.cols, data=result_data)

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise ValueError("Можно умножать только на число")
        result_data = [
            [self.data[i][j] * scalar for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(self.rows, self.cols, data=result_data)


if __name__ == "__main__":
    m1 = Matrix(3, 3)
    m2 = Matrix(3, 3)

    print("Матрица 1:\n", m1)
    print("\nМатрица 2:\n", m2)

    print("\nСумма матриц:\n", m1 + m2)

    print("\nМатрица 1 * 5:\n", m1 * 5)

    print("\nМатрица 1 == Матрица 2?", m1 == m2)
