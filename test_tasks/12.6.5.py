
# Напишите программу, которая определяет, является ли строка, введённая пользователем, палиндромом.

string = input().replace(' ', '').lower()

for i in range(len(string) // 2):
    if string[i] != string[-1-i]:
        print('Это не палиндром')
        break
else:
    print('Это палиндром')
