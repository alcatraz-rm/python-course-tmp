"""
Правильно
"""

def solve(a,b,c):
    return (a <= b) <= ((not a) and c)
print("a b c f")
for a in [0,1]:
    for b in [0,1]:
        for c in [0,1]:
            print(a,b,c,int(solve(a,b,c)))
