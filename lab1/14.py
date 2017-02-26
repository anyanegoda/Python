def non_empty(func):
    def wrapper():
        my_list = func()
        print('Исходная строка: ', my_list)
        my_list = list(filter(None, my_list))
        print('Строка без пустых строк: ', my_list)
    return wrapper

@non_empty
def get_pages():
    return ['chapter1', '', 'contents', '', 'line1']

get_pages()
