"""
Правильно

1. Функцию delen(n, m) можно сократить до одной строки:
    def delen(n, m):
        return n % m == 0
    Аналогичное упрощение работает для функций one, two, three;
2. Рекомендую не усложнять код, повышается вероятность допустить ошибку. В данном случае формула задачи
    может быть записана так: (delen(x, a) and delen(x, 12)) <= (delen(x, 42) or (not delen(x, 12))).
"""


def delen(n, m):
    if n%m==0:
        return 1
    else:
        return 0

def one(x, a):
    if delen(x, a)==1 and delen(x, 12)==1:
        return 1
    else:
        return 0

def two(x):
    if delen(x, 42)==1 or delen(x, 12)==0:
        return 1
    else:
        return 0

def three(x, a):
    if one(x, a)==1 and two(x)==0:
        return 0
    else:
        return 1

def four(a):
    d=1
    for x in range(1, 100000):
        if three(x, a)==0:
            d=0
            return 0
    if d==1:
        return 1
        
for a in range(1, 1000):
    if four(a)==1:
        print(a)
        break
