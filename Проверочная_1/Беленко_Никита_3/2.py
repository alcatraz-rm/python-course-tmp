"""
Правильно

1. Для импликации рекомендую использовать <=;
2. Программа проводит много лишних вычислений: она проверяет все x для всех значений A, в то время как
    можно заканчивать проверку иксов в тот момент, когда для какого-то из них формула оказалась неверна, и
    переходить к рассмотрению следующего значения A.
"""


def imp(a, b):
    if(a == 1 and b == 0):
        return 0
    else:
        return 1

def mod(a, b):
    if(a % b == 0):
        return 1
    else:
        return 0

mx = 0
for A in range (1, 1000):
    f = True
    for x in range (1, 1000):
        if not(imp((not(mod(x, A)) and mod(x, 6)), not(mod(x, 3)))):
            f = False
    if(f == True):
        if(mx < A):
            mx = A
print(mx)