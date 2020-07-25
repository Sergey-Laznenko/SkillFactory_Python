'''
надо написать простую игру, в которой программа загадывает число, а игрок его угадывает;
если угадать число не получилось, дается еще несколько ограниченных попыток.
'''

from random import randint as rand

number = rand(1, 100)

for guessesTaken in range(10):
    guess = int(input(f'Колличество попыток: {10 - guessesTaken}. Введите число: '))
    if guess < number:
        print(f'Число которое вы ввели, меньше')
    if guess > number:
        print(f'Число которое вы ввели, больше')
    if guess == number:
        print(f'Вы угадали число за {guessesTaken}')
        break
else:
    print('Попытки закончились')