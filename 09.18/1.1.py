from random import randint


class Generator:
    # ИСПРАВИТЬ: не "из девяти случайных чисел", а ...?
    """Класс, генерирующий список из девяти случайных чисел"""
    @staticmethod
    def generate(count: int):
        return [randint(1, 9) for _ in range(count)]

class Splitter:
    """Принимает двумерный список и разбивает его на все возможные одномерные списки."""
    @staticmethod
    def split(array) -> list:
        result = []

        row_count = len(array)
        col_count = len(array[0])

        for r in range(row_count):
            the_row = []
            for c in range(col_count):
                the_row.append(array[r][c])
            result.append(the_row)

        for c in range(col_count):
            the_col = []
            for r in range(row_count):
                the_col.append(array[r][c])
            result.append(the_col)

        diag1 = []
        diag2 = []

        for c in range(col_count):
            for r in range(row_count):
                if c == r:
                    diag1.append(array[r][c])
                r2 = row_count - r - 1
                if c == r2:
                    diag2.append(array[r][c])

        result.append(diag1)
        result.append(diag2)

        return result


class Verifier:
    """Принимает двумерный список и проверяет, что сумма чисел любого из содержимых списков одинакова."""
    @staticmethod
    def verify(arrays) -> bool:
        first = sum(arrays[0])

        for i in range(1, len(arrays)):
            if sum(arrays[i]) != first:
                return False

        return True


class MagicSquareGenerator:
    """Фасад для формирования магического квадрата.
    Генерирует магический квадрат заданного размера.
    """
    def __init__(self, num: int):
        self.num = num
        self.generator = Generator()
        self.splitter = Splitter()
        self.verifier = Verifier()

    def generate_magic_square(self):
        """Генерирует магический квадрат"""
        while True:
            matrix = [self.generator.generate(self.num) for _ in range(self.num)]
            if self.verifier.verify(self.splitter.split(matrix)):
                return matrix



msg = MagicSquareGenerator(3)
magic_sq = msg.generate_magic_square()
for number in magic_sq:
    print(number)

# stdout:
"""
[3, 1, 2]
[1, 2, 3]
[2, 3, 1]
"""


# ИТОГ: отлично — 6/6
