"""
Правильно

1. Делители можно искать не до n // 2 + 1, а до n^(1/2) + 1. Тогда сложность функции уменьшится n^(1/2)/2 раз.
"""


def prm(n):
    for i in range (2, n//2 + 1):
        if(n % i == 0):
            return 0
    return 1

cnt = 1
for i in range(4837177, 4837236):
    if(prm(i)):
        print(cnt, i)
        cnt += 1