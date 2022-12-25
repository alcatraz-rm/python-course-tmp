"""
Пока не буду комментировать, постарайтесь доделать, чтобы работало)
"""


def is_prime(n):
    if n % 2 == 0 and n != 2:
        return False
    for i in range(3, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fun(n):
    c = 0
    for i in range(2, n):
        if is_prime(i) == True:
            if n % i == 0:
                c = c + 1
                while n % i != 0:
                    n / i
            if c > 2:
                return False
    if c == 2:
        return True
    return False

k = 0
S = 0
for x in range(3, 15):
    if fun(x) == True:
        print(x, fun(x))
        k = k + 1
        S = S + x

print('S = ', S)
print('k = ', k)

print('среднее арифметическое:', S/k)
