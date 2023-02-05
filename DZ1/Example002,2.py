x = int(input('Введите Х: '))
y = int(input('Введите Y: '))

if x == 0 or y == 0:
    print('X ≠ 0 и Y ≠ 0')
elif x > 0 and y > 0:
    print(1)
elif x > 0 and y < 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x < 0 and y > 0:
    print(4)