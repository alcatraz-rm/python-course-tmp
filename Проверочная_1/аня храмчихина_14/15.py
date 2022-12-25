"""
Правильно
"""


count=0
for a in range(80,200+1):
    if all((((((x&56)!=0)or(x&43)!=0))<=((x&a)!=0)) for x in range(1,1000)):
        count+=1
print(count)
