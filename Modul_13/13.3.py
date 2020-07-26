'''
Напишите функцию, которая бы вычисляла число Фибоначчи на определенном шаге.
'''

def fibonacci(n):
    if n < 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

number = int(input(f'Введите число: '))
print(f'Число Фибоначчи, которое соответствует номеру {number}, это: {fibonacci(number)}')

