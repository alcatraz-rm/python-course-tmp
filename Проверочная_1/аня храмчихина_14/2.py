"""
Неправильно

1. Требуется вывести все строки таблицы истинности, у вас же только те, для которых формула выполняется;
2. Проверьте внимательно все импликации в вашей формуле;
3. Значение функции тоже требуется вывести, см. формат вывода таблицы в формулировке задачи.
"""


print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((w<=y)and((x>=z)==(y<=x))):
                    print(x,y,z,w)
                    