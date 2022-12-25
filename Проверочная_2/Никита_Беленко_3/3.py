"""
Почти правильно

1. Ответ правильный, но не очень понятно, где вы запоминаете наименьшее значение x. Вы скорее запоминаете наименьшее
    значение (a-b). Тут вероятно есть взаимосвязь между значением a-b и x, но лучше писать более явно;
3. Старайтесь избегать min в качестве названия переменной, такое название совпадает со встроенной функцией min.
"""


min = 100000

for x in range (13):
    a = int(f'8{x}121', 13)
    b = int(f'7{x}575', 13)
    if((a - b) % 19  == 0):
        if(min > (a - b) % 19):
           min = (a - b)

print(min / 19)

# 1464