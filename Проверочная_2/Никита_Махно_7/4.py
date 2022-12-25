"""
Правильно

1. Можно не ставить скобки в if, если условия простые.
"""


def F(a):
    if(a<=1):
        return 3
    else:
        return F(a-1)+2*F(a-2)-5

print(F(22))

#answer 1398104