"""
Правильно
"""


def funk(n):
    if n <=1:
        return 3
    return funk(n-1)+2*funk(n-2)-5
print(funk(22))
