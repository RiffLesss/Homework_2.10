#  Указанную денежную сумму разменять купюрами номиналом (500, 200, 100) рублей,
#  а также монетами номиналом (10,5, 2, 1)рублей.


try:
    amount = int(input('Введите сумму '))
except ValueError:
    print('Ошибка! Изначальная сумма должна быть числом.')
else:
    if amount > 0:
        count_500 = 0
        count_200 = 0
        count_100 = 0
        count_10 = 0
        count_5 = 0
        count_2 = 0
        count_1 = 0
        while amount >= 500:
            amount -= 500
            count_500 += 1
        while amount >= 200:
            amount -= 200
            count_200 += 1
        while amount >= 100:
            amount -= 100
            count_100 += 1
        while amount >= 10:
            amount -= 10
            count_10 += 1
        while amount >= 5:
            amount -= 5
            count_5 += 1
        while amount >= 2:
            amount -= 2
            count_2 += 1
        while amount >= 1:
            amount -= 1
            count_1 += 1
        if count_500 > 0 or count_200 > 0 or count_100 > 0:
            print('Купюры: ')
            if count_500 > 0:
                for i in range(count_500):
                    print(500, end=' ')
            if count_200 > 0:
                for i in range(count_200):
                    print(200, end=' ')
            if count_100 > 0:
                for i in range(count_100):
                    print(100, end=' ')
            print()
        if count_10 or count_5 or count_2 or count_1:
            print('Монеты: ')
            if count_10 > 0:
                for i in range(count_10):
                    print(10, end=' ')
            if count_5 > 0:
                for i in range(count_5):
                    print(5, end=' ')
            if count_2 > 0:
                for i in range(count_2):
                    print(2, end=' ')
            if count_1 > 0:
                for i in range(count_1):
                    print(1, end=' ')
    else:
        print('Ошибка! Изначальная сумма должна быть положительной.')


#   Сумма присвоить ввод с клавиатуры
#   Если Сумма не число, то
#       Вывести 'Ошибка! Изначальная сумма должна быть числом.'
#   Иначе
#       Если Сумма больше 0
#           Счётчик_500 присвоить 0
#           Счётчик_200 присвоить 0
#           Счётчик_100 присвоить 0
#           Счётчик_10 присвоить 0
#           Счётчик_5 присвоить 0
#           Счётчик_2 присвоить 0
#           Счётчик_1 присвоить 0
#           Пока Сумма больше 500
#               Уменьшить Сумму на 500
#               Увеличить Счётчик_500 на 1
#           Пока Сумма больше 200
#               Уменьшить Сумму на 200
#               Увеличить Счётчик_200 на 1
#           Пока Сумма больше 100
#               Уменьшить Сумму на 100
#               Увеличить Счётчик_100 на 1
#           Пока Сумма больше 10
#               Уменьшить Сумму на 10
#               Увеличить Счётчик_10 на 1
#           Пока Сумма больше 5
#               Уменьшить Сумму на 5
#               Увеличить Счётчик_5 на 1
#           Пока Сумма больше 2
#               Уменьшить Сумму на 2
#               Увеличить Счётчик_2 на 1
#           Пока Сумма больше 1
#               Уменьшить Сумму на 1
#               Увеличить Счётчик_1 на 1
#           Если Счётчик_500 больше 0 или Счётчик_200 больше 0 или Счётчик_100 больше 0, то
#               Вывести "Купюры:"
#               Если Счётчик_500 больше 0, то
#                   Вывести значение Счётчик_500 и надпись "купюр по 500 рублей"
#               Если Счётчик_200 больше 0, то
#                   Вывести значение Счётчик_200 и надпись "купюр по 200 рублей"
#               Если Счётчик_100 больше 0, то
#                   Вывести значение Счётчик_100 и надпись "купюр по 100 рублей"
#           Если Счётчик_10 больше 0 или Счётчик_5 больше 0 или Счётчик_2 больше 0 или Счётчик_1 больше 0, то
#               Вывести "Монеты:"
#               Если Счётчик_10 больше 0, то
#                   Вывести значение Счётчик_10 и надпись "монет по 10 рублей"
#               Если Счётчик_5 больше 0, то
#                   Вывести значение Счётчик_5 и надпись "монет по 5 рублей"
#               Если Счётчик_2 больше 0, то
#                   Вывести значение Счётчик_2 и надпись "монет по 2 рубля"
#               Если Счётчик_1 больше 0, то
#                   Вывести значение Счётчик_1 и надпись "монет по 1 рублю"
#       Иначе
#           Вывести 'Ошибка! Изначальная сумма должна быть положительной.'
