"""
Правильно

1. Название переменной sum совпадает со встроенной функцией sum, лучше не допускать таких коллизий.
"""


for A in range (10000):
    sum=1
    for x in range (10000):
        f = ((x & 26 != 0) or (x & 13 != 0)) <= ((x & 5 == 0) <= (x & A !=0))
        if f == 0:
            sum= 0
            break
    if sum == 1:
        print(A)
        break