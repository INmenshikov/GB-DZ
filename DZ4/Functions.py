import random
import controller
import math

    
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

def sign_heck(a):
    if a > -1:
        return f'+ {a}'
    else:
        return f'- {a * (-1)}'

def exponent_str(exponent):
    polynomial_ctr = ''
    if exponent == 0: print("Задайте натуральную степень отличную от нуля!")
    else: 
        i = 0 
        while exponent > -1:
            if i == 0:
                r_namber = random.randint(-100,100)
                while r_namber == 0:
                    r_namber = random.randint(-100,100)
                i += 1
                polynomial_ctr += f'{r_namber}*x**{exponent} '
                exponent -= 1
            else: r_namber = random.randint(-100,100) 
            if exponent > 1:
                polynomial_ctr += f'{sign_heck(r_namber)}*x**{exponent} '
                exponent -= 1
            elif exponent == 1:
                polynomial_ctr += f'{sign_heck(r_namber)}*x '
                exponent -= 1
            elif exponent == 0:
                polynomial_ctr += f'{sign_heck(r_namber)} = 0'
                exponent -= 1         
    return polynomial_ctr