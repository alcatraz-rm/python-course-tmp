"""
Правильно

1. Можно не указывать параметры 0 и 1 в функции range, они там по умолчанию, т.е. вместо range(0, 2, 1) можно написать
    range(2).
"""


print ('x y z w f')
for x in range (0,2,1):
    for y in range (0,2,1):
        for z in range (0,2,1):
            for w in range (0,2,1):
                f = ((x <= y) and (y <= z)) and ( z <= w )
                print (x, y, z , w, f)