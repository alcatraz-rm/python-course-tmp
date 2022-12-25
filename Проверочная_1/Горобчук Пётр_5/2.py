"""
Правильно
"""


for a in range(1000):
    b=True
    for x in range(1000):
        f = ((x & 28 !=0) or (x & 45 != 0)) <= ((x & 17 ==0) <= (x &a != 0))
        if not f:
            b= False
            break
    if b:
        print(a)
        break