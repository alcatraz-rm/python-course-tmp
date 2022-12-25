"""
Правильно

1. Программа выводит все подходящие числа, в то время как требуется только одно - наибольшее;
2. Рекомендую для импликации использовать <=.
"""


def imp(a, b):
    if (a == 1 and b == 0):
        return 0
    return 1

def f(x, A):
    a = (x & A) != 0
    b = (x & 39) == 7
    c = imp(a, b)
    d = (x & 30) != 6
    return int(c or d)

for A in range(10000):
    ok = 1
    for x in range(10000):
        if f(x, A) == 0:
            ok = 0
            break
    if (ok):
        print(A)
