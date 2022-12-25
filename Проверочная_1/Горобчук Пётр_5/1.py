"""
Правильно

1. range(0, 2, 1) - это то же самое, что и range(2), параметры 0 и 1 там стоят по умолчанию;
2. Вместо not(z) лучше писать not z.
"""


print('x y z w')
for x in range(0,2,1):
    for y in range(0, 2, 1):
        for z in range(0, 2, 1):
            for w in range(0, 2, 1):
                f = (w or ((x<=y) and ((not(z))<=x)))
                print(x,y,z,w,int(f))