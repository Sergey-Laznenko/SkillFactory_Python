"""
Задача: пользователь вводит произвольное целое число, а программа читает некий русский текст из файла
и зашифровывает его в другой файл со сдвигом, соответствующим этому числу.
"""

alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphaUp = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
number = int(input('Введите число, на которок нужно сдвинуть текст: '))

summary = ''


def change_char(char):
    if char in alpha:
        return alpha[(alpha.index(char) + number) % len(alpha)]
    elif char in alphaUp:
        return alphaUp[(alphaUp.index(char) + number) % len(alphaUp)]
    else:
        return char


with open('cezar.txt', encoding='utf8') as myFile:
    for line in myFile:
        for char in line:
            summary += change_char(char)

with open('cezarDone.txt', 'w', encoding='utf8') as myFile:
    myFile.write(summary)
