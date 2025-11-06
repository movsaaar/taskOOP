import random

class Matrix:
    def __init__(self, rows, cols, min_val=0, max_val=9):
        self.rows = rows
        self.cols = cols
        # Генерация случайных чисел
        self.data = [
            [random.randint(min_val, max_val) for _ in range(cols)]
            for _ in range(rows)
        ]

    def display(self):
        for row in self.data:
            print('\t'.join(map(str, row)))

    def save_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("Матрица:\n")
            for row in self.data:
                f.write('\t'.join(map(str, row)) + '\n')
            f.write(f"\nСумма всех элементов: {self.sum_elements()}\n")

    def sum_elements(self):
        total = 0
        for row in self.data:
            total += sum(row)
        return total


def main():
    rows = 4
    cols = 5

    matrix = Matrix(rows, cols)

    print("Сгенерированная матрица:")
    matrix.display()

    total = matrix.sum_elements()
    print(f"\nСумма всех элементов матрицы: {total}")

    filename = "matrix_output.txt"
    matrix.save_to_file(filename)
    print(f"\nМатрица и сумма сохранены в файл: {filename}")


if __name__ == "__main__":
    main()
