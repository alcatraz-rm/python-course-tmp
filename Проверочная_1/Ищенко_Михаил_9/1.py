"""
Правильно

1. Можно не указывать 0 в качестве левой границы диапазона в range, он там по умолчанию.
"""


print ("x y z w f")
for x in range (0,2):
    for y in range (0,2):
        for z in range (0,2):
            for w in range (0,2):
                 f = x or (not y or z or not w) and (y or not z)
                 print (x, y, z, w, f)
