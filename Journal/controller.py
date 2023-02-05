import view
import model

def start():
    a = 1
    while a == 1:
        try:
            model.set_class(view.input_class())
            model.set_subject(view.input_sabject())
            model.open_file()
            a = 0
        except:
            view.input_error()
        
    while True:
        journal = model.get_journal()
        view.list_of_child(journal)
        student = view.who_anser()
        if student =='exit':
            break
        mark = int(view.what_mark())
        model.student_mark(student, mark)
    model.save_file()