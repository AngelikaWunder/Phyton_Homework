# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12
from random import randint
n = int(input('Введите количество элементов первого множества n: '))
m = int(input('Введите количество элементов второго множества m: '))
my_list1=list()
my_list2=list()
for i in range(n):
    my_list1.append(randint(-20, 20))
print(my_list1)    
for i in range(m):
    my_list2.append(randint(-20, 20))
print(my_list2)   
my_list1=set(my_list1) 
my_list2=set(my_list2)
my_list_union = my_list1.union(my_list2)
my_list_union = list(my_list_union)
temp = 1
for i in range(len(my_list_union)-1):
    for j in range(len(my_list_union)-i-1):
        if my_list_union[j] > my_list_union[j+1]:
            my_list_union[j], my_list_union[j+1] = my_list_union[j+1], my_list_union[j]
  
print (my_list_union)