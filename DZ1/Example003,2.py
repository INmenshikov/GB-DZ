x1 = int(input('Введите Х1: '))
y1 = int(input('Введите Y1: '))
x2 = int(input('Введите Х2: '))
y2 = int(input('Введите Y2: '))
if x1 == x2 and y1 == y2:
    print('точки совпадают')
else:
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    print(distance)
