"""
Правильно

1. Можно не указывать параметры 0 и 1 в функции range, они там по умолчанию, т.е. вместо range(0, 2, 1) можно написать
    range(2);
2. Вместо проверки if f == False можно конвертировать f в int: int(f). Тогда f всегда будет 0/1.
"""


for x in range(0,2,1):
    for y in range(0,2,1):
        for z in range(0,2,1):
            f=((x or (not y) or (not z)) and (x or y or (not z)) and (x or y or z))
            if (f == False):
                f = 0
            print(x,y,z,f)