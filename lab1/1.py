a = input("Введите число: ")
print('Введенное число: ', a)
try:
    a = float(a)
except ValueError:
    print('Вводите цифры!')
else:
    try:
        a = str(a)
        r = a.split('.')
        if a.find('-') == -1:
            print(r[0] + ' руб. ' + r[1] + ' коп.')
        else:
            raise ValueError
    except ValueError:
        print('Некоректное число')