day_week = int(input("Введите номер дня недели: "))
if 0 < day_week < 8:
    if day_week > 6:
        print ('Да')
    else:
        print ('Нет')
else:
    print ('Не правильный ввод')
    