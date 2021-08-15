#8.1.  Реализовать класс «Дата»,
# функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
class Number(int):
    def __str__(self):
        return f"{self:02}"

class Date:
    date_attrs = ('day', 'month', 'year')

    def __init__(self, date: str, /):
        day, month, year = self.transform(date.split('-'))

        if not self.validate(day, month, year):
            raise ValueError(f"{date} invalid date format")

        self.day = day
        self.month = month
        self.year = year

    def __iter__(self):
        for attr in self.date_attrs:
            yield self.__getattribute__(attr)

    @classmethod
    def transform(cls, date):
        return [Number(i) for i in date]

    @staticmethod # метод статический

    def validate(*date):

        if not all(map(lambda x: isinstance(x, int), date)):
            return False

        day, month, year = date
        return all([1 <= day <= 31, 1 <= month <= 12, year >= 1980]) #'Валидный год 1980'

    def __str__(self):
        return f"Date is '{'-'.join([str(s) for s in self])}'"


if __name__ == '__main__':
    try:
        print(Date('01-12-2021'))
        print(Date('01-12-1981'))
    except ValueError as e:
        print(e)

# 8.2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.

class MyZeroDivisionError(Exception):
    text = "Деление на ноль запрещено"

    def __str__(self):
        return self.text


class Number(float):
    def __truediv__(self, other):
        if other is not None and not other:
            raise MyZeroDivisionError

        return Number(float(self) / float(other))


if __name__ == '__main__':
    while True:
        try:
            dividend, divider = map(Number, input("Введите делимое и делитель через пробел: ").split())
            print(dividend / divider)
        except MyZeroDivisionError as e:
            print(e)
        except ValueError as e:
            print(e)
            break

# 8.3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.

class NotNumberError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


if __name__ == '__main__':
    new_list = []

    while True:
        user_input = input("Введите требуемое количество чисел, для заполнения списка, или 'stop' для выхода: ")

        if user_input == "stop":
            break

        try:
            if not user_input.isdigit():
                raise NotNumberError(f"'{user_input}' has not numerical format")

            new_list.append(int(user_input))
        except NotNumberError as e:
            print(e)

    print(new_list)

# 8.4. Начните работу над проектом «Склад оргтехники».

class Storage:
    pass


class OfficeEquipment:
    vat = 0.13
    added_value = 2.0
    retail_rate = 1.3

    def __init__(
            self,
            eq_type: str,
            vendor: str,
            model: str,
            color: str,
            purchase_price: float,
    ):
        self.type = eq_type
        self.vendor = vendor
        self.model = model
        self.color = color

        self.purchase_price = purchase_price

        self.printable = True if self.type in ("printer", "HP") else False
        self.scannable = True if self.type in ("scanner", "HP") else False

    @property
    def retail_price(self):
        return self.wholesale_price * self.retail_rate

    @property
    def wholesale_price(self):
        return self.purchase_price * (1 + self.vat) * (1 + self.added_value)

    def __str__(self):
        return f"{self.type} {self.vendor} {self.model} ({self.color})"


class Printer(OfficeEquipment):
    printable = True
    scannable = False

    def __init__(self, *args):
        super().__init__('Принтер', *args)


class Scanner(OfficeEquipment):
    printable = False
    scannable = True

    def __init__(self, *args):
        super().__init__('scanner', *args)


class Xerox(OfficeEquipment):
    printable = True
    scannable = True

    def __init__(self, *args):
        super().__init__('HP', *args)


if __name__ == '__main__':
    p1 = Printer("Epson", "L-222", "black", 9000)
    print(p1)

#8.7. Реализовать проект «Операции с комплексными числами».

class MyComplex:
    def __init__(self, real, imag=0):
        self.__complex = complex(real, imag)

    def __add__(self, other):
        if isinstance(other, MyComplex):
            other = other.__complex

        complex_ = self.__complex + other
        return MyComplex(complex_.real, int(complex_.imag))

    def __mul__(self, other):
        if isinstance(other, MyComplex):
            other = other.__complex

        complex_ = self.__complex * other
        return MyComplex(complex_.real, int(complex_.imag))

    def __str__(self):
        return self.__complex.__str__()


if __name__ == '__main__':
    c1 = MyComplex(4, -2)
    c2 = MyComplex(7)

    print(c1 + c2, complex(4, -2) + complex(7))
    print(c1 * c2, complex(4, -2) * complex(7))




# 8.5.





