"""
Не совсем правильно

1. Программа выводит все подходящие значения, в то время как требуется только одно - наибольшее (к тому же, в конце стоит
    вывод значения a, поэтому в конце программа выводит 999, что вообще не является верным ответом);
2. В задаче сказано, что x - натуральное число, то есть перебор иксов надо начинать с 1, а не с 0;
3. Шаг 1 стоит в range по умолчанию, то есть вместо range(a, b, 1) можно писать просто range(a, b);
4. Ваше логическое выражение можно записать в одну строку:
    int(x % 18 == 0) <= (int(x % 54 == 0) <= int(x % A == 0)).
"""


flag = 1
x=1
for a in range (1,10000,1):
    flag=0
    for x in range (0,1000,1):
        di=0
        dii=0
        diii=0
        if(x%18 == 0):
            di=1
        if(x%54 == 0):
            dii=1 
        if(x%a == 0):
            diii=1
            
        f=int(dii <= diii) >= di
        if(f==0):
            flag=1
    if(flag == 0):
        print (a)
print (a)