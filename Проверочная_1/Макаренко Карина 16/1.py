"""
Правильно
"""


print('x', 'y', 'z','w','f')
for y in range(2):
    for x in range(2):
        for z in range(2):
            for w in range(2):
                f = (w<=z) and ((y<=x)==(z<=y))
                print (x, y, z, w, f)