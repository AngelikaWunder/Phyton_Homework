# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4
def sum (num_A, num_B):
    if num_B == 0:
        return num_A
    return sum(num_A+1, num_B-1)

n = int(input('Введите целое неотрицательное число A =  '))
if n < 0:
    n = int(input('Ваше число отрицательное. Введите целое неотрицательное число A =  '))
m = int(input('Введите целое неотрацательное число B = '))
if m < 0:
    m = int(input('Ваше число отрицательное. Введите целое неотрицательное число В =  '))
print(f'Сумма двух чисел А и В равна: {sum(n, m)}')