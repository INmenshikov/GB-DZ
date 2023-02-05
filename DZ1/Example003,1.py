namber = int(input('Введите номер четверти: '))
if namber < 1 or namber > 4:
    print('Введите число от 1го до 4ех')
elif namber == 1:
    print('x > 0 and y > 0')
elif namber == 2:
    print('x > 0 and y < 0')
elif namber == 3:
    print('x < 0 and y < 0')
elif namber == 4:
    print('x < 0 and y > 0')