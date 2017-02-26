text = ('www.orange.com', 'www.panda', 'www.temp.ru', 'oooops')
for s in text:
    s = str(s)
    if s.startswith('www.', 0, 4):
        s = 'http://' + s
        if s.endswith('.com'):
            print(s)
        else:
            s = s + '.com'
            print(s)