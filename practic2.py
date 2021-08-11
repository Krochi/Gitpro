class Cell:
    def __init__(self, count: int):
        self._count = count

    def __add__(self, other: "Cell") -> "Cell":
        return Cell(self._count + other._count)

    def __sub__(self, other: "Cell") -> "Cell":
        if self._count > other._count:
            return Cell(self._count - other._count)

        # raise ValueError(f"{self._count} - {other._count}: impossible operation")
        print(f"{self._count} - {other._count}: impossible operation")

    def __mul__(self, other: "Cell") -> "Cell":
        return Cell(self._count * other._count)

    def __truediv__(self, other: "Cell") -> "Cell":
        return Cell(self._count // other._count)

    def make_order(self, per_row: int) -> str:
        rows, tail = self._count // per_row, self._count % per_row
        return '\n'.join(['*' * per_row] * rows + (['*' * tail] if tail else []))

    def __str__(self) -> str:
        return f"Клетка состоит из {self._count} ячеек"


if __name__ == '__main__':
    c1 = Cell(17)
    print(c1)
    c2 = Cell(13)
    print(c2)

    print(c1 + c2)
    print(c1 - c2)
    print(c2 - c1)
    print(c2 - c2)
    print(c1 * c2)
    print(c1 / c2)
    print((c1 * c2).make_order(23))
