def main_menu():
    commands = ['Показать все контакты',
                'Открыть файл',
                'Сохранить файл',
                'Новый контакт',
                'Изменить контакт',
                'Удалить контакт',
                'Найти контакт',
                'Выйти из программы',]
    print(f'\n Выберите пунк меню: ')
    for i in range(len(commands)):
        print(f'\t{i + 1}. {commands[i]}')
    user_imput = int(input(f'\n Введите пункт меню: '))
    return user_imput

def load_success():
    print('Телефонная книга загружена успешно')

def save_succes():
    print('Телефонная книга сохранена успешно')

def new_contact():
    name = input('Введиет Имя и Фамилию контакта: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий к контакту: ')
    return name, phone, comment