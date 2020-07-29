




from random import randint

total_round = int(input(f'Введите кол-во раундов: '))
rounds = 1
win_m = 0       # Победы Михаила
win_c = 0       # Победы Криса

if 1 <= total_round <= 100:                     # кол-во раундов
    while total_round > rounds :                # задаём цикл равный введённому
        for i in range(total_round):
            mishka = randint(1,6)               # Генерируем бросок Михаила
            cris = randint(1,6)                 # Генерируем бросок Криса
            print()
            print('--Start--')
            print(f' Результат Михаила - ', mishka)                       # Результат Михаила
            print(f' Результат Криса - ',cris)                         # Результат Криса
            if mishka > cris:
                print('-= Mishka won =-')
                win_m += 1                      # кол-во побед Михаила
            elif mishka < cris:
                print('-= Cris won =-')
                win_c += 1                      # кол-во побед Криса
            else:
                print ('-= Draw =-')
                
            rounds += 1                         # Счётчик раундов
        if win_m > win_c:                       # Сравниваем кол-во побед Михаила
            print()
            print('Победитель Мишка')
            print('Выйграл за ', win_m, 'раунда')
        elif win_m < win_c:                     # Сравниваем кол-во побед Криса
            print()
            print('Победитель Крис')
            print('Выйграл за ', win_c, 'раунда')
        else:
            print()
            print('Победила дружба')


            
