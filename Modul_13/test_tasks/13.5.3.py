'''
Написать программу, которая принимает на вход от пользователя целое число — это будет длина ряда чисел,
которые являются факториалами своего индекса.
'''

def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n

number = int(input('Введите число: '))
row = []

for i in range(number + 1):
    if i % 2 != 0:
        row.append(factorial(i))

Sum = 0
for j in row:
    Sum += j

print(f'Сумма всех цифр факториала, состоящих на нечётных позициях длинной {number}, равна:{Sum}')
