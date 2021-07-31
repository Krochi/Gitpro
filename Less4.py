#4.1 Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
def sal():
    try:
        time = int(input('Выроботка в часах:'))
        salary = int(input('Ставка:'))
        bonus = int(input('Премия:'))
        res = time * salary + bonus
        print(f'заработная плата сотрудника {res}')

    except ValueError:
        return print('Отсутствует число')
sal()

#4.2 Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
num_list = [3, 14, 5, 67, 3, 8]
new_list = [num for num in num_list if num > num_list[num_list.index(num)-1]]
print(new_list)

#4.3 Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21
print(f'предел чисел от 20 до 240 {[num for num in range(20,240) if num % 20 == 0 or num % 21 == 0]}')

#4.4 Представлен список чисел. Определить элементы списка, не имеющие повторений.

my_list = [1, 1, 5, 6, 3, 8,8 , 6]
new_list = [num for num in my_list if my_list.count(num) == 1]
print(new_list)

#4.5 Реализовать формирование списка, используя функцию range() и возможности генератора.
from functools import reduce
def new_func(elem_prev, num):
    return elem_prev * num
print(f'Чётные значения {[num for num in range(99, 1001) if num % 2 == 0]}')
print(f'Результат вычесления всех элементов списка {reduce(new_func, [num for num in range(99, 1001) if num % 2 == 0])}')

#4.6 Реализовать два небольших скрипта:
from itertools import count
for num in count(int(input('Введите стартовое число: '))):
    print(num)
    #break

from itertools import cycle
my_list = [True, 'Tree', 123]
for num in cycle(my_list):
    print(num)
    #break

#4.7 Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
def fibo_gen(number):
    count = 1
    while count <= number:
        yield count
        count += 1
i = 1
first_fifteen = []
for num in fibo_gen(5):
    if i > 15:
        break
    else:
        first_fifteen.append(num)
        i += 1
print(first_fifteen)