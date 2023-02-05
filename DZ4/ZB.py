# B. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

import controller
import math
import Functions
controller.create_file(2,2)
file_a = open('./ДЗ4/file_1.txt', 'r')
str_a = ''
for i in file_a:
    str_a += i       
file_b = (open('./ДЗ4/file_2.txt', 'r'))
str_b = ''
for i in file_b:
    str_b += i
print(str_a)
print(str_b)

def str_replace(str_1):
    str_1 = str_1.replace(' ','').replace('-','+-').replace('**2','').replace('*','').replace('x','').replace('=0','').split('+')
    print(str_1)
    a = int(str_1[0])
    b = int(str_1[1])
    c = int(str_1[2])
    discrim = b ** 2 - 4 * a * c
    if discrim > 0:
        m1 = (-b + math.sqrt(discrim)) / (2 * a)
        m2 = (-b - math.sqrt(discrim)) / (2 * a)
        return m1 + m2
    elif discrim == 0:
        m = -b / (2 * a)
        return m
    else:
        return 0


print(f'Сумма корней многочленов = {str_replace(str_a) + str_replace(str_a)}')


