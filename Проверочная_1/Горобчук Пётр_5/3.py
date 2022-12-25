"""
Неправильно

1. Есть ошибка в алгоритме решения задачи: вы проверяете, что число имеет ровно один делитель, который меньше либо
    равен квадратному корню из a. Если это так, то счетчик увеличивается. Ошибка состоит в том, что если найденный
    делитель строго меньше квадратного корня из а, то есть еще один делитель, который строго БОЛЬШЕ квадратного
    корня из a. Вы его заведомо не найдете, так как проверяете числа до квадратного корня. Получается, что делителя
    уже 2 и такое число нам не подходит.
2. Получается, чтобы был только один натуральный делитель, не равный 1 и самому числу, он должен равняться
    квадратному корню из этого числа. Значит, число должно быть квадратом некоторого натурального числа. Заведомо
    можно рассматривать только квадраты натуральных чисел в диапазоне [3361, 33626].
3. Среди этих квадратов вам надо найти те, которые не имеют других натуральных делителей, кроме корня из них.
    Чтобы других делителей не было, нужно, чтобы корень из этого числа был простым.
4. То есть по итогу вам нужно найти все числа, квадраты которых лежат в диапазоне [3361, 33626], и вывести, сколько
    простых чисел среди них. Их будет 25.
"""


c =0
for a in range(3661,33626,1):
    b=[]
    for n in range(2,int(a**0.5)+1):
        if a%n==0:
            b+=[n]
    if len(b)==1:
        c+=1
print(c)