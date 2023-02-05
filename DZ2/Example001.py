# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Пример:
# 6782 -> 23
# 0,56 -> 11
number = input('Введите число: ')
number = number.replace('.','')
sum_namber = 0
input_number = int(number) 
while input_number != 0:
    sum_namber += input_number % 10
    input_number //= 10
print(f'Сумма цифр равна: {sum_namber}')



