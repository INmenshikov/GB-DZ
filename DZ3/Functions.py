import random

def generating_sheet_random_numbers(a,b,c):
    lst = []
    for i in range(c):
        lst.append(random.randint(a,b))
    return lst

def generating_bunch_random_number(a,b,c):
    bun = set()
    while len(bun) < c:
        g = random.randint(a,b)
        bun.add(str(g))   
    return bun

def fibonacci(n):
    if  n == 0:
        return 0
    if n in (1, 2):
        return 1
    if n < 0:
        return (-1) ** (-n + 1) * fibonacci(-n)
    return fibonacci(n - 1) + fibonacci(n - 2)