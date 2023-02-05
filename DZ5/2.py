# Создайте программу для игры в ""Крестики-нолики""

def draw_field(namber_field):  # рисует игровое поле
    print("." * 13)
    for i in range(3):
        print(":", namber_field[0 + i * 3], ":", namber_field[1 + i * 3], ":", namber_field[2 + i * 3], ":")
        print("." * 13)

def input_validation(player_in):  # принимает ввод пользователя
    valid = False
    while not valid:
        answer = input(f'Куда поставим {player_in}?: ')
        try: 
            answer = int(answer)
        except:
            print("Введите число!")
            continue
        if answer > 0 and answer < 10:
            if (str(namber_field[answer - 1]) not in "XO"):
                namber_field[answer - 1] = player_in
                valid = True
            else:
                print("Клетка занята!")
        else:
            print("Введите число от 1 до 9")

def check_victory(namber_field):  # проверяет, выиграл ли игрок
    winning_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in winning_combinations:
        if namber_field[i[0]] == namber_field[i[1]] == namber_field[i[2]]:
            return namber_field[i[0]]
    return False

namber_field = list(range(1, 10))
counter = 0
win = False
while not win:
    draw_field(namber_field)
    if counter % 2 == 0:
        input_validation("X")
    else:
        input_validation("O")
    counter += 1
    if counter > 4:
        tmp = check_victory(namber_field)
        if tmp:
            print(tmp, "победил!")
            win = True
            break
    if counter == 9:
        print("Ничья!")
        break

