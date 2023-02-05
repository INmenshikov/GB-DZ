#Напишите программу, которая найдёт произведение пар чисел списка. 
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

lst = [2, 3, 4, 5, 6]
if len(lst) % 2:
    length = len(lst) // 2 + 1
else:
    length = len(lst) // 2
resalt = []
buffer = len(lst)
for i in range(length):
    resalt.append(lst[i] * lst[buffer - 1])
    buffer -= 1
print(f'{lst} => {resalt}')
