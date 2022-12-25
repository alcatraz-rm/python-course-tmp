"""
Правильно
"""


maxx=0
for n in range(100):
    b_n = bin(n)
    if b_n.count("1") % 2 ==0:
        b_n+="00"
    else:
        b_n+="10"
    b_n = b_n[2:]
    b_n = int(b_n,2)
    if b_n < 125 and b_n > maxx:
        maxx = b_n
print("--------",maxx)
