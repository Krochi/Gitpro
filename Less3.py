#3.1 Реализовать функцию, принимающую два числа
def div(*args):
    try:
        a = int(input('Введите первое число:'))
        b = int(input('Введите второе число:'))
        rez = a/b
    except ValueError:
        return 'ValueError'
    except ZeroDivisionError:
        return 'На ноль делить нельзя!'
    return rez
print(f'result {div()}')

#3.2 Реализовать функцию, принимающую несколько параметров
def ind_person (name, lastname, year, city, email, tele):
    return ''.join([name, lastname, year, city, email, tele])
print(ind_person(name = 'Ivan', lastname = 'Ivanov', year = '1900', city = 'Kaluga', email = 'adress@mail.com', tele = '8 800 000 00 0'))

#3.3 Реализовать функцию my_func()
def my_func(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3

print(f'Result - {my_func(int(input("Введите первый аргумет: ")), int(input("Введите второй аргумент: ")), int(input("Введите третий аогумент: ")))}')

#3.4 Программа принимает действительное положительное число x и целое отрицательное число y

def my_func(x: int, y: int):
    #return 1 / x ** abs(y)
    return x ** y
print(my_func(5, -14))

#3.5 Программа запрашивает у пользователя строку чисел, разделенных пробелом.
def my_sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Введите число or Q для выхода - ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Текущее значение: {sum_res}')
    print(f'Итоговое значение: {sum_res}')


my_sum()
#3.6Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text
def int_func (*args):
    word = input("Введите слова: ")
    print(word.title())
    return
int_func()


