"""
Правильно

1. Можно не писать скобки у return, то есть можно написать просто return ans.
"""


def f(x):
    s=str(x)
    m=[]
    for i in range(3):
        m.append(int(s[i])+int(s[i+1]))
    if m[0]==min(m):
        ans=int(str(max(m[1], m[2]))+str(min(m[1], m[2])))
    elif m[1]==min(m):
        ans=int(str(max(m[0], m[2]))+str(min(m[0], m[2])))
    else:
        ans=int(str(max(m[1], m[0]))+str(min(m[1], m[0])))
    return(ans)

for i in range(1000, 10000):
    if f(i)==126:
        print(i)
        break
