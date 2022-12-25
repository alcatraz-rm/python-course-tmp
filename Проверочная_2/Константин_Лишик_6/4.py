"""
Правильно
"""


f=[]
f.append(0)
f.append(2)
for i in range(2, 40):
    f.append(f[i-1]+5*i**2)

print(f[39])
