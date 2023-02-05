
import random
a = 1
b = 100
c = 5

def generating_sheet_random_numbers(a,b,c): # было
    lst = []
    for i in range(c):
        lst.append(random.randint(a,b))
    return lst

lst = [random.randint(a,b) for i in range(c)]   #стало


