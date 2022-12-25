"""
Правильно
"""


for x in range(10,100,1):
    y = ''
    y += str(x % 4)
    y += str(x % 2)
    y += str(x % 3)
    c = int(y)
    if c == 112:
        print(x)
        break