
def input_class():
    return input ('С каким классом работаем? ').upper()

def input_sabject():
    return input ('Какой предмет? ').lower()
    
def input_error():
    print('Ошибка ввода')

def who_anser():
    return input('Кто будет отвечать? ')

def what_mark():
    return input('На какую оценку ответил? ')

def list_of_child(journal: dict):
    for i, child in enumerate(journal, 1):
        print(f'{i}. {child:20}{journal.get(child)}')
