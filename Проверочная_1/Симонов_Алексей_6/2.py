"""
Неправильно

1. В задании была функция ДЕЛ(n, m), у вас вместо нее стоит побитовая конъюнкция, из-за этого формула
    получается совсем другой;
2. Программа проводит много лишних вычислений: она проверяет все x для всех значений A, в то время как
    можно заканчивать проверку иксов в тот момент, когда для какого-то из них формула оказалась неверна, и
    переходить к рассмотрению следующего значения A;
3. Рекомендую для импликации использовать <=.
"""


for A in range(1,40000):
    ans = 0
    for x in range(1,50000):
        if (not(((x & A) !=0) and ((x & 15) ==0)) or  (((x & 18) !=0) or ((x & 15) != 0))):
            ans+=1
    if ans == 49999:
        print(A)
