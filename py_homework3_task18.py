# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5
from random import randint
my_list = []
lens = int(input('Введите количество элементов в списке N: '))
for i in range(lens):
    my_list.append(randint(0, 100))
print (f'ваш список из {lens} элементов: {my_list} ')
number_x = int(input('Введите натуральное число X: '))

my_list_less = [] # формируем список чисел меньших, чем Х
my_list_more = [] # формируем список чисел больших, чем Х
for item in range(lens):
    if my_list[item] < number_x:
        my_list_less.append(my_list[item])
    elif my_list[item] > number_x:
        my_list_more.append(my_list[item])
print(my_list_less)
print(my_list_more)
max_from_less = my_list_less[0] # задаем макс-число из списка чисел меньших, чем Х
min_from_more = my_list_more[0] # задаем мин-число из списка чисел больших, чем Х
i=0
while i <= (len(my_list_less)-1) :
    if my_list_less[i] > max_from_less:
        max_from_less = my_list_less[i] 
    i+=1
j=0        
while j <= (len(my_list_more)-1) :
    if my_list_more[j] < min_from_more:
        min_from_more = my_list_more[j]
    j+=1
# print(max_from_less)
# print(min_from_more)
# сравниваем найденные числа между собой; находим, какое ближе к Х 
if (number_x - max_from_less) < (min_from_more - number_x): 
    print (f'Самый близкий по величине элемент к числу Х: {max_from_less}')
elif (number_x - max_from_less) > (min_from_more - number_x):
    print (f'Самый близкий по величине элемент к числу Х: {min_from_more}')  
else:
    print (f'Самые близкие по величине элементы к числу Х: {min_from_more} и {max_from_less}') 