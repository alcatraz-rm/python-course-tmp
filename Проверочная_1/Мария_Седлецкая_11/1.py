"""
Правильно, хорошее решение

1. Круто, что использовали itertools.product;
2. Лучше выводить значение функции единообразно, то есть либо везде 0/1, либо True/False. У вас где-то так,
    а где-то иначе.
"""


from itertools import product
def fun(x, y, z):
    return((x or y) and (not x or y or not z))

print('x y z F')

for x, y, z in product({0,1}, repeat = 3):
    print(x, y, z, fun(x, y, z) )
