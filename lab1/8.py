import math
import random
n = random.randint(1, 100)
print("Количество элементов массива: ", n)
lg = math.log(n, 2)
lg = math.ceil(lg)
lg = math.pow(2, lg)
lg = int(lg)
m = [random.randint(1, 100) for x in range(n)]
print(m)
print('Ближайшая свеерху степень двойки: ', lg)
a = lg - n
print('Не хватает нулей: ', a)
m.append([0] * a)
print(m)