"""
Правильно

1. Значение логического выражения можно сохранить в переменную и избавиться таким образом от if/else.
    Например, так:
    f = ((y <= x) and z and (not(z == y)))
    print(x, y, z, f)
"""


#1
#(y <= x) and z and (not(z == y)) 
print('x y z f')
for x in range (2):
    for y in range(2):
        for z in range(2):
                if ((y <= x) and z and (not(z == y))) == False:
                    print(x, y, z, 0)
                else:
                    print(x, y, z, 1)