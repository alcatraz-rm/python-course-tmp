"""
Правильно

1. Лучше везде использовать один тип кавычек, либо одинарные, либо двойные;
2. Можно не ставить скобки в if, если условия простые.
"""


s=185*'3'

while "9999" in s or "333" in s:
    if("9999" in s):
        s=s.replace("9999","3",1)
    else:
        s=s.replace("333","99",1)

print(s)

#answer 9933