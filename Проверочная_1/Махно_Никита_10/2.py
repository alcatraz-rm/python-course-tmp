"""
Правильно

1. Два вложенных if'a можно объединить и написать так: if flag and A > mx;
2. Если условия в if простые, то можно не ставить скобки.
"""


mx = -1
for A in range(100):
    flag = True
    for x in range(100):
        if (((x & 30 == 0) or (x & 43 == 0)) <= ((x & 19 != 0) <= (x & A == 0))) == 0:
            flag = False
    if (flag == True):
        if (A > mx):
            mx = A

print(mx)

# answer=10