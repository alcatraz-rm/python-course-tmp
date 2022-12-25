"""
Правильно

1. Можно не писать == True, то есть вместо if A == True можно просто написать if A, но в целом пишите так, как вам понятнее;
2. В целом, значение выражения можно сохранить в переменную и вывести ее значение вместе с переменными, тогда можно
    избавиться от if/else. Например, вот так:
    f = (not(x) and y and z) or ((not(x) and y and not(z)) or (not(x) and not(y) and not(z)))
    print(x, y, z, int(f))
"""


print("((not(x) and y and z) or ((not(x) and y and not(z)) or (not(x) and not(y) and not(z)))")
print('x y z')                           
for x in range (2):                      
    for y in range(2):  
        for z in range(2):               
                if (not(x) and y and z) or ((not(x) and y and not(z)) or (not(x) and not(y) and not(z))) == True:
                    print(x, y, z, 1)  
                else:
                    print(x, y, z, 0)