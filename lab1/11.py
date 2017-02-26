def frange(start, stop, step):
    x = start
    my_list = []
    if step > 0:
        while x < stop:
            my_list.append(round(x, 1))
            x += step
    else: # if step < 0
        while x > stop:
            my_list.append(round(x, 1))
            x += step
    return my_list

for f in frange(1, 5, 0.1):
    print(f, ' ', end='')
