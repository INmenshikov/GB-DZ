
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: 
# На столе лежит заданное количество конфет. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'
import random
print(f"Приветвую, давайте разделим наши конфеты в игровой форме! ")
player_1 = input("Как Вас зовут? ")
bot_ = input("Напишите один если хотитче чтобы с вами сыграл я или играйте с другом: ")
if bot_ != "один":
    player_2 = input("Как зовут 2 игрока? ")
    general_candies = int(input("Сколько у нас конфет? ")) # сдесь можно сделать функцию с проверкой числа, 
    # но чтобы не усложнять будем считать что игроки без зачатков тестировщиков
    print(f"Приступим. {player_1}, {player_2} У вас {general_candies} конфет.")
    print("Правила:")
    print("За один ход можно забрать не более чем 28 конфет.")
    print("Все конфеты оппонента достаются сделавшему последний ход.")
    r_nam = random.randint(0,10)
    if r_nam > 5: 
        print(f"Первым ходит {player_1}.")
        r_nam = 1 
    else: 
        print(f"Первым ходит {player_2}.")
        r_nam = 0


    while general_candies > 28:
        if r_nam == 1:
            number_candies = int(input(f"Сколько конфет берет {player_1}? "))
            if number_candies > 28:
                print("Не больше 28 конфет за раз. Не хорошо нарушать правила ")
                number_candies = int(input(f"Сколько конфет берет {player_1}? "))
            general_candies = general_candies - number_candies
            print(f"Конфет осталось {general_candies}")
            r_nam = 0
        else:
            number_candies = int(input(f"Сколько конфет берет {player_2}? "))
            if number_candies > 28:
                print("Не больше 28 конфет за раз. Не хорошо нарушать правила ")
                number_candies = int(input(f"Сколько конфет берет {player_2}? "))
            general_candies = general_candies - number_candies
            number_candies = 0
            print(f"Конфет осталось {general_candies}")
            r_nam = 1     
    else:
        if r_nam == 0:
            print(f"Оставшиется {general_candies} достаются {player_2} и он выигрывает эту игру!!! ")
            print(f"Поздравляем {player_2} тебе достались все конфеты!!!")
            print(f"р/с {player_2} надеюсь ты не будешь жадничать и поделишься с {player_1}")
        else:
            print(f"Оставшиется {general_candies} достаются {player_1} и он выигрывает эту игру!!! ")
            print(f"Поздравляем {player_1} тебе достались все конфеты!!!")
            print(f"р/с {player_1} надеюсь ты не будешь жадничать и поделишься с {player_2}")
else:
    bot_1 = input("Напишите 'глупый' и я буду поддаваться: ")
    if bot_1 == 'глупый':
        general_candies = int(input("Сколько у нас конфет? ")) # сдесь можно сделать функцию с проверкой числа, 
        # но чтобы не усложнять будем считать что игроки без зачатков тестировщиков
        print(f"Приступим. {player_1} у Нас {general_candies} конфет.")
        print("Правила:")
        print("За один ход можно забрать не более чем 28 конфет.")
        print("Все конфеты оппонента достаются сделавшему последний ход.")
        r_nam = random.randint(0,10)
        if r_nam > 5: 
            print(f"Первым ходит {player_1}.")
            r_nam = 1 
        else: 
            print(f"Первым ходит многоуважающий диктор.")
            r_nam = 0


        while general_candies > 28:
            if r_nam == 1:
                number_candies = int(input(f"Сколько конфет берет {player_1}? "))
                if number_candies > 28:
                    print("Не больше 28 когфет за раз. Не хорошо нарушать правила ")
                    number_candies = int(input(f"Сколько конфет берет {player_1}? "))
                general_candies = general_candies - number_candies
                print(f"Конфет осталось {general_candies}")
                r_nam = 0
            else:
                number_candies = random.randint(0,28)
                print(f"Диктор берет {number_candies} конфет ")
                general_candies = general_candies - number_candies
                number_candies = 0
                print(f"Конфет осталось {general_candies}")
                r_nam = 1     
        else:
            if r_nam == 0:
                print(f"Оставшиется {general_candies} достаются диктору и он выигрывает эту игру!!! ")
                print(f"Поздравляем диктору достались все конфеты!!!")
                print(f"р/с Я не ем конфеты можешь оставить их себе")
                
            else:
                print(f"Оставшиется {general_candies} достаются {player_1} и он выигрывает эту игру!!! ")
                print(f"Поздравляем {player_1} тебе достались все конфеты!!!")
        print(f"концевка глупова бота")
    else:
            general_candies = int(input("Сколько у нас конфет? ")) # сдесь можно сделать функцию с проверкой числа, 
            # но чтобы не усложнять будем считать что игроки без зачатков тестировщиков
            print(f"Приступим. {player_1} у Нас {general_candies} конфет.")
            print("Правила:")
            print("За один ход можно забрать не более чем 28 конфет.")
            print("Все конфеты оппонента достаются сделавшему последний ход.")
            r_nam = random.randint(0,10)
            if r_nam > 5: 
                print(f"Первым ходит {player_1}.")
                r_nam = 1 
            else: 
                print(f"Первым ходит многоуважающий диктор.")
                r_nam = 0

            
            while general_candies > 56:
                if r_nam == 1:
                    number_candies = int(input(f"Сколько конфет берет {player_1}? "))
                    if number_candies > 28:
                        print("Не больше 28 когфет за раз. Не хорошо нарушать правила ")
                        number_candies = int(input(f"Сколько конфет берет {player_1}? "))
                    general_candies = general_candies - number_candies
                    print(f"Конфет осталось {general_candies}")
                    r_nam = 0
                else:
                    if general_candies < 56:
                        c = int(general_candies / 28)
                        if general_candies > c * 28:
                            number_candies = (general_candies - (c * 28)) - 1
                        else:
                            number_candies = 28
                    else:
                        c = int(general_candies / 28)
                        if general_candies > c * 28:
                            number_candies = general_candies - (c * 28)
                        else:
                            number_candies = 28
                    print(f"Диктор берет {number_candies} конфет ")
                    general_candies = general_candies - number_candies
                    number_candies = 0
                    print(f"Конфет осталось {general_candies}")
                    r_nam = 1     
            else:
                if r_nam == 0:
                    print(f"Оставшиется {general_candies} достаются диктору и он выигрывает эту игру!!! ")
                    print(f"Поздравляем диктору достались все конфеты!!!")
                    print(f"р/с Я не ем конфеты можешь оставить их себе")
                else:
                    print(f"Оставшиется {general_candies} достаются {player_1} и он выигрывает эту игру!!! ")
                    print(f"Поздравляем {player_1} тебе достались все конфеты!!!")
            print(f"Концевка умного бота")