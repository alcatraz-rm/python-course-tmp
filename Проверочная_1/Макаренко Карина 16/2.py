"""
Почти правильно

1. Аккуратнее с функцией range, она не учитывает правую границу отрезку, если бы только число 125 подходило, то
    оно бы потерялось;
2. В условии сказано, что x - натуральное число, то есть перебор должен начинаться с 1, т.е. надо range(1, 1000) вместо
    range(1000);
3. Как только вы нашли какой-то x, для которого формула неверна, то остальные можно не перебирать, т.е. после k=1
    можно дописать break.
"""


def funk(x,a):
    return((x&56!=0)or(x&43!=0))<=(x&a!=0)
for a in range(75,125):
    k=0
    for x in range(1000):
        if not funk(x,a):
            k=1
    if k==0:
        print (a)
        break