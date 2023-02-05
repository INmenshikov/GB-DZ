# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для и получения случайного int
import random
from Functions import *

len_list = int(input('Введите длинну списка: '))
my_list = generating_sheet_random_numbers(0,99,len_list)
print(my_list)
i = 0
end_list = []
while i < len_list:
    ri = random.randint(0,len(my_list)-1)
    end_list.append(my_list[ri])
    my_list.pop(ri)
    ri = None
    i += 1
print(end_list)






