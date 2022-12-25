"""
Правильно

1. В коде можно было не писать == True, т.е. вместо if A == True можно просто написать if A;
2. Вместо not(x) лучше писать not x;
3. В целом можно было обойтись без if и написать так (а лучше логическое выражение вынести в отдельную функцию):
    print(x, y, z, int(((x or y or not(z))and (not(x)or y or not(z)) and(not(x) or not(y) or z)))).
"""


print("x y z f")
for x in range(2):
    for y in range(2):
        for z in range(2):
            if ((x or y or not(z))and (not(x)or y or not(z)) and(not(x) or not(y) or z)) == True:
                print(x,y,z,1)
            else:
                print(x,y,z,0)
