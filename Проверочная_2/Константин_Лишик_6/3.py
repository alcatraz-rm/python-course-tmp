"""
Правильно

1. Алгоритм решения правильный, по мнению авторов, ответ 25871. Видимо они имели ввиду, что разность должна быть
    неотрицательной, но не написали это. Думаю, в ЕГЭ не должно быть такой неоднозначности.
"""


m=[]
for x in range(22):
    for y in range(13):
        n=int(f'{x}23{x}5', 22)-int(f'67{y}9{y}', 13)
        if n%57==0:
            print(int(n/57))
