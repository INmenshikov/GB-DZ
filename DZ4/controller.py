import Functions
import controller 
def create_file (c,d):
    a = Functions.exponent_str(c)
    b = Functions.exponent_str(d)
    with open('./ДЗ4/file_1.txt', 'w') as data:
        data.write(a)
    with open('./ДЗ4/file_2.txt', 'w') as data:
        data.write(b)
    
    