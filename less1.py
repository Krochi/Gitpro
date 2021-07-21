# Задание 1
# 1.1 Вычесляем площадь комнаты
#length = float(input('Введите длину комнаты (м):'))
#width = float(input('Введите ширину комнаты(м):'))
#area = length * width
#name = input('Введите имя:')
#print(f"Привет {name.title()} , площадь твоей комнаты {area}")

# 1.2 Переводим время
#seconds_in_hour = 3600
#seconds_in_minute = 60
#seconds = int(input('Введите секунды:'))
#hours = seconds // seconds_in_hour
#seconds = seconds - (hours * seconds_in_hour)
#minutes = seconds // seconds_in_minute
#seconds = seconds - (minutes * seconds_in_minute)
#print(f'Ваш результат {hours:0d}:{minutes:02d}:{seconds:02d}')

# 1.3 Число n
#n = int(input('Введите число:'))
#num = n * 123
#print(num)

# 1.4 Целое число
#i = int(input('Введите целое число:'))
#ls = []
#while i > 10:
    #ls.append(i % 10)
    #i //= 10
#num = max(ls)
#print(num)

# 1.5 Выручка и прибыль
#a = float(input('Введите прибыль:')
#b = float(input('Введите издержки:'))
#c = a/b
#if a > b:
    #print(f'Фирма работает в прибыль {a/b:.2f}%')
    #crew =int(input('Введите количество сотрудников:'))
    #print(f'Прибыль на одного сотрудника {c/crew:.2f}%')
#elif a == b:
    #print('Фирма работате в ноль')
#else:
    #print('Фирма несёт убытки')

# 1.6 Про бегуна

a = int(input('Дистанция в первый день:'))
b = int(input('Введите желаемый :'))
first_day = 1
result = a
while result < b:
    a = a + 0.1
    result += 1
    result = result + a
print(f'Результат на %.d' % result)




