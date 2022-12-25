"""
Правильно

1. Можно не ставить скобки у условий в if и в while.
"""


s = "3" + "6"*120 + "3"
def f(a,b):
    global s
    if (a in s):
        s = s.replace(a,b,1)

while("63" in s or "664" in s or "6665" in s):
    f("63", "4")
    f("664", "5")
    f("6665", "3")
print(s)
