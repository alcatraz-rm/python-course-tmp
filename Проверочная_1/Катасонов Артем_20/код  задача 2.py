"""
Правильно, но есть замечание.

1. Выводите значение функции единообразно, у вас где-то 0/1, а где-то True/False.
"""


print('x y z w')

for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                  print(x, y, z, w, not(w) and(x and not(z) or not(x) and not(y) and z))