"""
Правильно
"""

print("x y z f")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            f = ((not(y or z) or x) or (x == z))
            print(x, y, z, int(f))