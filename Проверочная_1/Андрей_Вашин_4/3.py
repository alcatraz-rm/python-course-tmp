"""
Правильно

1. Алгоритм поиска числа делителей (findD) можно упростить: искать делители только до квадратного
    корня из n, для каждого из них всегда есть второй делитель больше квадратного корня из n.
    То есть если находим делитель, то к счётчику d можем сразу прибавить 2, так как точно есть второй делитель.
    Таким образом, сложность функции уменьшается в n^(1/2) раз;
2. Проверку, что значение есть среди ключей словаря, можно записать так: if a in numbers
    Запись if a in list(numbers.keys()) работает дольше, так как нужно взять все ключи и
    преобразовать их в список, это особенно трудоемко, если ключей много;
3. При поиске максимума среди ключей словаря можно не преобразовывать в list и не вызывать метод keys,
    т.е. можно написать так: m = max(numbers);
4. Максимальное число делителей m можно не искать после цикла, а запоминать сразу в цикле;
5. Можно даже не хранить словарь, который по числу делителей хранит все числа, имеющие столько делителей.
    Можно запоминать наибольшее количество делителей, которое нам встретилось. Если на каком-то шаге мы встретили
    число, у которого больше делителей, чем у какого-либо числа до этого, то обновляем наше количество делителей и
    начинаем запоминать все числа, имеющие столько делителей.
"""


def findD(n):
    d = 0
    for j in range(1,n+1):
        if n%j==0:
            d+=1
    return d

def findLastD(n):
    d = []
    for j in range(n+1, 0, -1):
        if n%j==0:
            d.append(j)
        if len(d)==2:
            return d

numbers = {}

for i in range(586132,586431):
    a = findD(i)
    if a in list(numbers.keys()):
        numbers[a].append(i)
    else:
        numbers[a] = [i]

m = max(list(numbers.keys()))
print(min(numbers[m]))
q = findLastD(min(numbers[m]))
print(m, q[0], q[1])

print(max(numbers[m]))
q = findLastD(max(numbers[m]))
print(m, q[0], q[1])
