# ; Задача 26: Напишите программу, которая на вход принимает
# ; два числа A и B, и возводит число А в целую степень B с
# ; помощью рекурсии.
# ; A = 3; B = 5 -> 243 (3⁵)
# ; A = 2; B = 3 -> 8
def multiplication (num_A, num_B):
    if num_B == 0:
        return 1
    if num_B < 0:
        return 1 / multiplication(num_A, -num_B)
    if num_B%2 == 0:
        return multiplication(num_A, num_B//2)*multiplication(num_A, num_B//2)
    else:
        return multiplication(num_A, num_B - 1)*num_A

n = int(input('Введите число A =  '))
m = int(input('Введите число B = '))
print(f' Число  А  в степени В равно {multiplication(n, m)}')
