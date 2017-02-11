string = input('Введите строку: ')
words = string.split()
print(words)
print('Результат: ')
for word in words:
    if word.istitle() == 1:
        word = word.upper()
    print(word, " ", sep='', end='', flush=True)