class ShortError(Exception):
    pass

s = input('Введите номер дебетовой карты: ')
try:
    s = int(s)
except ValueError:
    print('Вводите числа!')
else:
    try:
        s = str(s)
        if len(s) != 16:
            raise ShortError
    except ShortError:
        print('Введите 16 цифр!')
    else:
        print('Номер в скрытом виде: ' + s[0:4] + '*' * 12 + s[12:16])
