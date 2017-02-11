import random
a = [random.randint(1, 10) for x in range(3)]
print(a)
b = sorted(a)
print(b)
if a == b:
    print(True)
else:
    print(False)
