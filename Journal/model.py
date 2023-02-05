import os
journal = {}
subject = ''
path = ''

def set_class(class_path: str):
    global path
    
    list_file = []
    for root, dirs, files in os.walk("."):  
        for filename in files:
            list_file.append(filename)
    if class_path + '.txt' in list_file:
        path = 'Classes/' + class_path + '.txt'
    
    
def set_subject(our_subject: str):
    global subject
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for sub in file:
        if sub.split(';')[0] == our_subject:
            subject = our_subject
        elif sub.split(';')[0].startswith(our_subject) == True:
            subject = sub.split(';')[0]
    
def open_file():
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for sub in file:
        if sub.split(';')[0] == subject:
            for study in sub.split(';')[1].strip().split(', '):
                journal[study.split(':')[0]] = study.split(':')[1].split()
                
def get_journal():
    return journal

def student_mark(student: str, mark: int):
    if mark > 0 and mark < 6:
        marks = journal.get(student)
        marks.append(mark)
        journal[student] = marks
    elif mark < 1: 
        mark = 1
        marks = journal.get(student)
        marks.append(mark)
        journal[student] = marks
    elif mark > 5: 
        mark = 5
        marks = journal.get(student)
        marks.append(mark)
        journal[student] = marks

def save_file():
    new_file = []
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for sub in file:
        if sub.split(';')[0] != subject:
            new_file.append(sub.strip())
    item = []
    for student, marks in journal.items():
        item.append(student + ':' + ' '.join(list(map(str, marks))))
    item = subject + ';' + ', '.join(item)
    new_file.append(item)
    with open(path, 'w', encoding='UTF-8') as data:
        data.write('\n'.join(new_file))