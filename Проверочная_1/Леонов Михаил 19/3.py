"""
Не совсем правильно

1. Ваш ответ чуть больше верного, причина в том, что вы всегда не учитываете один из делителей числа.
"""


s = 0
k = 0
for a in range(2, 30001):
    s = 0
    for d in range(2, a // 2 + 1):
        if a % d == 0 and a != d:
            s = s + d
    if a > s:
        k += 1
print(k)
# ответ 22571
