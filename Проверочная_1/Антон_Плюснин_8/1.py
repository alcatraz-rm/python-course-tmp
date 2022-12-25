"""
Правильно

1. Формулу можно записать в одну строку: (x and (y or (not z)) and w) == (x <= ((not y) and z));
2. Рекомендую для импликации использовать <=.
"""


def imp(a, b):
    if (a == 1 and b == 0):
        return 0
    return 1

def f(x, y, z, w):
    a = (y or (not z))
    a = x and a and w
    b = (not y) and z
    b = imp(x, b)
    return int(a == b)

print("x y z w f")
print()

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                print(x, y, z, w, f(x, y, z, w))
