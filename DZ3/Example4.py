# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

namber = int(input('Введите число: '))
binary_number = ""
i = namber
while i > 0:
    binary_number = str(i % 2) + binary_number
    i = i // 2
print(f'{namber} -> {binary_number}')
