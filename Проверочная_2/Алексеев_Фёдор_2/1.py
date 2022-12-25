"""
Правильно

1. В целом, можно запоминать не все подходящие числа, а только максимальное.
"""


def solve(x):
    y = ""
    y += str(x%4)
    y += str(x%3)
    y += str(x%2)
    return int(y)
a = []
for i in range(10, 100):
    if(solve(i) == 220):
        a.append(i)
print(a[-1])
