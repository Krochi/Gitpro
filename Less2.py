# Задание 2
#2.1 Создать список.
#new_list = ['ship', 5, 6.7, -6, True]
#for my_list in range(len(new_list)):
    #print(type(new_list[my_list]))

#2.2 Реализовать обмен значений.
#new_elem = input('Введите элементы списка через пробел:')
#new_elem = new_elem.split()
#for elem in range(0, len(new_elem)-1, 3):
    #new_elem[elem], new_elem[elem+1] = new_elem[elem+1], new_elem[elem]
#print(new_elem)

#2.3 Определение времени года, по месяцу.
#season = ['зима', 'весна', 'лето', 'осень']
#season_dict = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
#month = int(input('Введите месяц по номеру:'))
#if month == 12 or month == 1 or month == 2:
    #print(season_dict.get(1))
    #print(season[0])
#elif month == 3 or month == 4 or month == 5:
    #print(season_dict.get(2))
    #print(season[1])
#elif month == 6 or month == 7 or month == 8:
    #print(season_dict.get(3))
    #print(season[2])
#elif month == 9 or month == 10 or month == 11:
    #print(season_dict.get(4))
    #print(season[3])
#else:
    #print('Это не месяц, пробуй ещё!')

2.4 #ВВести строку из нескольких слов
#words_str = input('Введите строку:')
#new_words = words_str.split()
#for index, words in enumerate(new_words, 1):
    #print(index, words[:10])

2.5 #Реализовать структуру "Рейтинг"
#my_list = [7, 5, 3, 3, 2]
#print(f"Рейтинг - {my_list}")
#digit = int(input("Введите число:"))
#while True:           #digit != 99:
    #for i in range(len(my_list)):
        #if my_list[i] == digit:
            #my_list.insert(i + 1, digit)
           # break
        #elif my_list[0] < digit:
            #my_list.insert(0, digit)
        #elif my_list[-1] > digit:
            #my_list.append(digit)
        #elif my_list[i] > digit and my_list[i + 1] < digit:
            #my_list.insert(i + 1, digit)
    #print(f"текущий список - {my_list}")
    #digit = int(input("Введите число "))

2.6 #Реализовать структуру данных «Товары»
empty_struct = []
while True:
    check = input('Введите y/n:')
    if check == 'y':
        new_dict = dict({'название': input('Введите название товара:'), 'цена': float(input('Введите цену:')), 'количество':
                         int(input('Введите кол-во:')), 'еденицы': input('Введите еденицу товара:')})
        empty_struct.append((len(empty_struct)+1, new_dict))
    elif check == 'n':
        break
    else:
        check = input('Пповторите ввод y/n:')
print(empty_struct)
################
list_dict = [
    (1, {'название': 'компьютер', 'цена': 200000, 'количество': 1, 'едениц': 'шт'}),
    (2, {'название': 'принтер', 'цена': 20000, 'количество': 1, 'едениц': 'шт'}),
    (3, {'название': 'бумага', 'цена': 200, 'количество': 5, 'едениц': 'упак'})

]
result = {}
for new_dict in list_dict:
    my_number, my_dict = new_dict
    for key, value in my_dict.items():
        value_dict = result.get(key, [])
        if value not in value_dict:
            value_dict.append(value)
        result[key] = value_dict
print(result)




