"""
Правильно

1. Для импликации рекомендую использовать <=;
2. Вместо not(a) лучше писать not a, без скобок.
"""


def imp(a, b):
    if(a == 1 and b == 0):
        return 0
    else:
        return 1

print("x", "y", "x", "f")
for x in range(2):
    for y in range(2):
        for z in range(2):
            print(x, y, z, end=" ")
            print(imp(x, not(z)) and (imp(not(y), x)))