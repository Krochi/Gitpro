# 5.1 Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем
#new_list = []
#while True:
    #line = input("Сделайте ввод: ")
    #if line == '':
        #print(new_list)
        #exit()
    #else:
        #newline = line + '\n'
        #new_list.append(newline)

    #with open("test.txt", "w") as file_obj:
        #file_obj.writelines(new_list)

# 5.2 Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
my_list = ['Имя\n', 'Фамилия\n', 'Отчество\n']
with open("test1.txt", 'w+') as file:
    file.writelines(my_list)
with open("test1.txt") as file:
    lines = 0
    letters = 0
    for line in file:
        lines += line.count("\n")
        letters = len(line)-1
        print(f"{letters} letters in line")
    print(f"String count is {lines}")

# 5.3 Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
firm = {'Иванов': 170, 'Петров': 210, 'Сидоров': 190, 'Аарансон': 150}
try:
    file = open("test2.txt", 'w')
    for last_name, salary in firm.items():
        file.write(last_name + ':' + str(salary) + "\n")
except IOError:
    print("Возникла ошибка ввода-вывода!")
finally:
    file.close()
summa = 0
count = 0
persons = []
with open("test2.txt", "r") as file:
    for line in file:
        print(line, end="")
        tokens = line.split(':')
        if int(tokens[1]) <= 200:
            persons.append(tokens[0])
        summa += int(tokens[1])
        count += 1
result = summa / count
print(f"persons: {persons}")
print(f"average: {result}")

# 5.4 Создать (не программно) текстовый файл со следующим содержимым:
dict_new = {'One': 'Один',
            'Two': 'Два',
            'Three': 'Три',
            'Four': 'Четыре'}
with open('test_3.txt', 'r') as file, open('test3.txt', 'w') as file_write:
    for line in file.readline():
        number = line.strip().split(' - ')
        file_write.write(f'{dict_new} - {number}\n')

print(dict_new)


# 5.5 Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
def summary():
    try:
        with open('test_4.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Ошибка ввода-вывода')
summary()

# 5.6 Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.


#5.7 Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
import json

profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('test_7.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует.')
    pr = {'средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('test_7.json', 'w') as write_js:
    json.dump(profit, write_js)



#6.1 Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
from time import sleep


class TrafficLight:
    lamp_color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i < 3:
            print(f'Светофор переключается \n '
                  f'{TrafficLight.lamp_color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(3)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()

#6.2 Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина)
class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return self._length * self._width


class MassCount(Road):
    def __init__(self, _length, _width, volume):
        super().__init__(_length, _width)
        self.volume = volume


r = MassCount(50, 10000, 150)
print(r.mass())

#6.3  Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход)

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')
        # return f'{sum(self._income.values())}'


a = Position('Arman', 'Roadrunner', 'foreman', 100000, 50000)
print(a.get_full_name())
print(a.position)
print(a.get_total_income())

#6.4  Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).

class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} начинает движение'

    def stop(self):
        return f'{self.name} останавливается'

    def turn_right(self):
        return f'{self.name} поворачивает направо'

    def turn_left(self):
        return f'{self.name} поворачивает налево'

    def show_speed(self):
        return f'Средняя скорость {self.name} это {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Средняя скорость для городских автомобилей  {self.name} это {self.speed}')

        if self.speed > 40:
            return f'превышение скорости {self.name} для городских автомобилей'
        else:
            return f'Нормальная скорость {self.name} для городских автомобилей'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Средняя скорость для комерческих автомобилей {self.name} это {self.speed}')

        if self.speed > 70:
            return f'Превышение скорости  {self.name} для комерческих автомобилей'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} для департамента управления полиции'
        else:
            return f'{self.name} не для департамента управления полиции'


Melkus = SportCar(100, 'Красная', 'Melkus', False)
Hyundai = TownCar(30, 'Серебристая', 'Hyundai', False)
ГАЗель_NEXT = WorkCar(70, 'Белая', 'ГАЗель_NEXT', True)
Chevrolet_Silverado_SSV = PoliceCar(110, 'Blue',  'Chevrolet_Silverado_SSV', True)
print(ГАЗель_NEXT.turn_left())
print(f'Когда {Hyundai.turn_right()}, {Melkus.stop()}')
print(f'{ГАЗель_NEXT.go()} с превышением скорости. {ГАЗель_NEXT.show_speed()}')
print(f'{ГАЗель_NEXT.name} это {ГАЗель_NEXT.color}')
print(f'{Melkus.name} полицейская машина? {Melkus.is_police}')
print(f'{Chevrolet_Silverado_SSV.name}  полицейская машина? {Chevrolet_Silverado_SSV.is_police}')
print(Melkus.show_speed())
print(Hyundai.show_speed())
print(Chevrolet_Silverado_SSV.police())
print(Chevrolet_Silverado_SSV.show_speed())

#6.5 Реализовать класс Stationery (канцелярская принадлежность).
class Stationery:
    atr_title = 'Title'
    def draw(self):
        print('Запуск отрисовки.')
class Pen(Stationery):
    def draw(self):
        print('Отрисовка ручкой')
class Pencil(Stationery):
    def draw(self):
        print('Отрисовка карандашом')
class Handle(Stationery):
    def draw(self):
        print('Отрисовка маркером')

my_pen = Pen()
my_pencil = Pencil()
my_handle = Handle()
my_pen.draw()
my_pencil.draw()
my_handle.draw()