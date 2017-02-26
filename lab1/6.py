text = input('Введите ваш текст: ')
unique_letters = set(text)
res = {}
for letter in unique_letters:
    if letter != ' ':
        res[letter] = text.count(letter)
        if text.count(letter) == 1:
            print(letter)

print(res)
