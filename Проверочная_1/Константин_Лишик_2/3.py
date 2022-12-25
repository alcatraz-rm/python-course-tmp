"""
Правильно

1. Делители можно искать не до i / 2, а до i^(1/2) + 1. Тогда сложность уменьшится i^(1/2)/2 раз.
"""


n=1

a=[]

for i in range(2532000, 2532161):
    j=2
    d=1
    
    while j<=i/2:
        if i%j==0:
            d=0
            break
        j+=1

    if d==1:
        a.append(i)
        n+=1

    if n==6:
        j=1
        for i in a:
            print(j, i)
            j+=1
        break
