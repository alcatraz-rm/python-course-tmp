"""
Правильно

1. Внутри цикла вместо if/else можно написать: c = int(f(x, y, z, w)).
"""


def f(x, y, z, w):
    return ((not x) and y and z) or ((not x) and (not y) and z) or ((not x) and (not y) and (not z))


print("x y z w f")
for x in [0, 1]:
    for y in [0, 1]:
        for w in [0, 1]:
            for z in [0, 1]:
                if(f(x,y,z,w)):
                    c=1
                else:
                    c=0
                print(x, y, z, w, c)
