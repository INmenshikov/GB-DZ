# Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

namber = int(input("Введите число: "))
my_list = [round((1 + 1/i) ** i,2) for i in range(1, namber + 1)]

print(f'Для n = {namber} -> {my_list}')
print(f'Сумма {sum(my_list)}')
exit()
def lis_nam(nam):     #было
    a = 0
    for i in range(1, nam + 1):
        a = (1 + 1/i) ** i
        yield round(a,2)

def sum_list(n):
    sum = 0.0
    for i in n:
        sum += i
    return sum 

namber = int(input("Введите число: "))
lis = list(lis_nam(namber))

print(f'Для n = {namber} -> {lis}')
print(f'Сумма {sum_list(lis)}')