import sys

def input_money(nom, s_sum):
    k = s_sum // nom
    if nom == 1000:
        s = '1000'
    if nom == 500:
        s = '500'
    if nom == 100:
        s = '100'
    if nom == 50:
        s = '50'
    if nom == 10:
        s = '10'
    if (money[s]) - k >= 0:
        out_money[s] = k
        s_sum -= k * nom
    else:
        out_money[s] = k
        s_sum -= (money[s]) * nom
    return s_sum


money = {'1000': 7, '500': 9, '100': 8, '50': 7, '10': 5}
#print(money)

out_money = {}
k = 0
input_sum = int(input("Введите нужную сумму: "))
if input_sum % 10 != 0:
    print("Сумма не кратна 10!")
    sys.exit(['Error'])
input_sum = input_money(1000, input_sum)
input_sum = input_money(500, input_sum)
input_sum = input_money(100, input_sum)
input_sum = input_money(50, input_sum)
input_sum = input_money(10, input_sum)

s = 0
if input_sum != 0:
    print("Операция не может быть выполнена!")
    sys.exit(['Error'])
else:
    for i in sorted(out_money.keys()):
        if out_money[i] != 0:
            print(i, '*', out_money[i], ' ', end='')