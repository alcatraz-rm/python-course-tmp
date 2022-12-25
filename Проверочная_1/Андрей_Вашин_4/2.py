"""
Неправильно

1. Неправильно написана функция импликации s(a, b);
    Импликация a -> b ложна только в том случае, если a = 1, b = 0, а здесь наоборот, при a = 0, b = 1.
    Для импликации удобно использовать <=, т.е. a -> b тогда и только тогда, когда a <= b.
    Если исправить это, то программа останавливается на 58 - это правильный ответ.
2. Программа выводит все подходящие числа, в то время как требуется только одно - наибольшее из них;
3. Рекомендую НЕ писать руками побитовую конъюнкцию (хотя круто, что вы можете это сделать),
    в Python она делается так же, как и в C: a & b.
    Формулу из задания можно записать так: (x & 30 != 4) or (int(x & 35 == 1) <= int(x & A == 0));
4. Если мы нашли какой-то x, для которого формула не верна (в цикле for), то дальше иксы можно не перебирать,
    нужно прервать выполнение с помощью break и перейти к рассмотрению следующего A, иначе программа делает
    много лишних проверок.
"""


def bc(a,b):
    ab = list(bin(a))[2:]
    ab.reverse()
    bb = list(bin(b))[2:]
    bb.reverse()
    cb = []
    if len(ab)>len(bb):
        minab = bb
    else:
        minab = ab
    for i in range(len(minab)):
        if int(ab[i])==1 and int(bb[i])==1:
            cb.append(1)
        else:
            cb.append(0)
    return toDecimal(cb)

def toDecimal(l):
    a = 0
    for x in range(len(l)):
        if l[x]==1:
            a += 2**x
    return a

def o(a,b):
    if a==1 or b==1:
        return 1
    return 0

def s(a,b):
    if a==0 and b==1:
        return 0
    return 1

def check(a,b,c,r):
    if bc(a,b)==c:
        if r==1:
            return 1
        else:
            return 0
    else:
        if r==1:
            return 0
        else:
            return 1


bo = True

for A in range(9999):
    for x in range(9999):
        if o(check(x,30,4,-1), s(check(x,35,1,1),check(x,A,0,1)))!=1:
            bo = False
    if bo:
        print(A)
    bo = True
        
