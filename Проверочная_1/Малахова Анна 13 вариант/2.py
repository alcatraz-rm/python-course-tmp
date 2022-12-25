"""
Почти правильно, есть важный момент.

1. В задаче сказано, что x - натуральное число, то есть перебор иксов надо начинать с 0, а не с 1.;
2. Функцию DEL можно упростить так:
    def DEL(n, m):
        return n % m == 0

3. Два вложенных if можно объединить:
    if f and A > Amax:
        Amax = A
4. Где-то я видел похожий код, с точностью до названия переменных и функций)
"""


def DEL(n,m):
    if n%m==0:
        return 1
    else:
        return 0 
 
Amax = 0
for A in range(1, 1000):
    f = True
    for x in range(1000):
        if ((not(DEL(x, A)) and DEL(x, 21)) <= DEL(x, 14)) == False:
            f = False
            break
    if f:
        if A>Amax:
            Amax = A
print (Amax)
               
