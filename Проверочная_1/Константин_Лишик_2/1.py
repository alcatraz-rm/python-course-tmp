"""
Правильно

1. Рекомендую не делать столько аналитической работы, повышается вероятность ошибки;
    Здесь вы по сути запрограммировали две части логического выражения, в голове вычислив, в каком случае
    каждая часть будет истинна/ложна. Можно записать это выражение более явно и в одну строку:
        ((x <= z) and (z <= w)) or (y == int(x or z));
2. Можно не создавать список a, а сразу итерироваться по генератору: for i in product([0,1], repeat=4);
3. Круто, что использовали product, а не вложенные циклы.
"""


from itertools import product

def one(x, z, w):
    if (x==1 and z==0) or (z==1 and w==0):
        return 0
    else:
        return 1

def two(x, y, z):
    if (y==1 and (x==1 or z==1)) or (y==0 and x==0 and z==0):
        return 1
    else:
        return 0

def three(x, y, z, w):
    if one(x, z, w)==1 or two(x, y, z)==1:
        return 1
    else:
        return 0

a=list(product([0,1], repeat=4))

print('x y z w f')

for i in a:
    print(i[0], i[1], i[2], i[3], three(i[0], i[1], i[2], i[3]))
