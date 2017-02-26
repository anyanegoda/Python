def extra_enumerate(arr):
    st = 0
    cum = 0
    for elem in arr:
        yield elem
        st += 1
        cum = cum + elem
        frac = cum * 0.1
        print('(', elem, ', ', cum,', ', frac,')')

x = [1, 3, 4, 2]
for i in extra_enumerate(x):
    print(end='')