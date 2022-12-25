"""
Правильно

1. Хорошее решение, без работы со строками;
2. Можно не ставить скобки в if.
"""


a = 5 + 3 * 15**2 + 2 * 15**3 + 1 * 15**4
b = 9 + 7 * 17**2 + 6 * 17**3

ans = 10**10
xa = -1
ya = 10000

for x in range(15):
    for y in range(17):
        val = (a + b + x * 15 + y * 17)
        if val % 131 == 0:
            if (ya > y):
                ans = val // 131
                xa = x
                ya = y
            ans = min(ans, val // 131)

print(ans)
