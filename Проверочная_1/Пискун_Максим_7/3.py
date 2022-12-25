"""
Неправильно (предварительно)

1. В задании необходимо вывести сумму делителей и наибольший нетривиальный делитель. У вас выводятся все делители
    искомого числа (но число и делители находятся правильно).
    Есть предположение, что программа выдает правильный ответ случайно;
2. Функция delet, по логике решения, для заданного числа должна возвращать 4 делителя, если их действительно 4. Если это
    не так, то она вернет [999999999999999999,1]. Но кажется, что ее реализация работает неправильно. Примером является
    число 27 - его делители это 1, 3, 9, 27. Но функция для него возвращает [999999999999999999,1].
"""


def delet(a):
    ans = True
    k = -1
    for i in range(2,a//2+1):
        if a % i ==0:
            k = i
            break
    if k ==-1:
        return [999999999999999999,1]
    for i in range(2,a//k//2+1):
        if (a//k) % i==0:
            ans = False
            break
    if ans == True:
        return([1,k,a//k,a])
    return [999999999999999999,1]

maxx = 0
minn = 99999999999999999
for i in range(573213,575341):
    j = sum(delet(i))
    if j< minn:
        g = i
        minn = j
print(delet(g))
#[1, 593, 967, 573431]
# 574992 967
