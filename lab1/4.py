string = input('Введите строку: ')
words = string.replace(',', ' ').replace('.', ' ').split()
print(words)

def sort_length(input_str):
    return len(input_str)

words = sorted(words, key=sort_length, reverse=True)

for item in words:
    print(item)
