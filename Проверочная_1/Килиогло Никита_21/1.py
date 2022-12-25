"""
Правильно

1. Условие можно задать менее громоздко, если убрать == 1. Можно записать условие из задачи так:
    ((not x) or y or z) and ((not x) or (not y) or z) and ((not x) or (not y) or (not z));
2. Будьте аккуратны со столбцами, у вас они в необычном порядке - x y w z, обычно x y z w;
3. Кажется, значение функции лучше выводить в виде 0/1, а не True/False, но тут поступайте как вам удобно;
4. Заголовки столбцов тоже помогут при дальнейшем анализе таблицы.
"""


def f(x, y, z, w):
    return((not x == 1 or y == 1 or z == 1) and (not x == 1 or not y == 1 or z == 1) and (not x == 1 or not y == 1 or not z == 1))

for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                print(x, y, w, z, f(x, y, z, w))
