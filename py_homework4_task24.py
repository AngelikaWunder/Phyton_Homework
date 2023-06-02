# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
# 4 -> 1 2 3 4
# 9
from random import randint
count_of_bushes = int(input('Введите количество кустов на грядке n = '))
my_list = []
for i in range(count_of_bushes):
    my_list.append(randint(1, 50))
print(my_list)    
max_berries = 0
i=0
sum_on_3_brushes = 1
# while i+2 <= count_of_bushes-1:
#     sum_on_3_brushes = my_list[i]+my_list[i+1]+my_list[i+2]
#     if sum_on_3_brushes > max_berries:
#         max_berries = sum_on_3_brushes
#     i+=1
# sum_on_3_brushes = my_list[count_of_bushes-2]+my_list[count_of_bushes-1]+my_list[0] 
# if sum_on_3_brushes > max_berries:
#         max_berries = sum_on_3_brushes
# sum_on_3_brushes = my_list[count_of_bushes-1]+my_list[0]+my_list[1] 
# if sum_on_3_brushes > max_berries:
#         max_berries = sum_on_3_brushes 

for i in range(count_of_bushes):
    if i+2 <= count_of_bushes-1:
        sum_on_3_brushes = my_list[i]+my_list[i+1]+my_list[i+2]
        if sum_on_3_brushes > max_berries:
            max_berries = sum_on_3_brushes
    elif i+2 == count_of_bushes:
        sum_on_3_brushes = my_list[count_of_bushes-2]+my_list[count_of_bushes-1]+my_list[0] 
        if sum_on_3_brushes > max_berries:
            max_berries = sum_on_3_brushes
    else:
        sum_on_3_brushes = my_list[count_of_bushes-1]+my_list[0]+my_list[1] 
        if sum_on_3_brushes > max_berries:
            max_berries = sum_on_3_brushes        
  
print (f'модуль соберет за один заход максимальное количество ягод: {max_berries}')   




