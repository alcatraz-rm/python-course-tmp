"""
Правильно

1. Вы сначала проверяете само логическое выражение, а потом его отрицание, чтобы вывести 0/1 в качестве значения
    функции. Но достаточно один раз вычислить это значение, сохранив в отдельную переменную.
    Например, код мог бы выглядеть так:
    f = ((x <= w) or y and (not(z))) and ((y <= (not(z))) or x and (not(w)))
    print(x, y, z, w, f)
"""


print('x y z w f')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if ((x <= w) or y and (not(z))) and ((y <= (not(z))) or x and (not(w))):
                    print(x, y, z, w, 1)
                if not(((x <= w) or y and (not(z))) and ((y <= (not(z))) or x and (not(w)))):
                    print(x, y, z, w, 0)
# ответ
# x y z w f
# 0 0 0 0 1
# 0 0 0 1 1
# 0 0 1 0 1
# 0 0 1 1 1
# 0 1 0 0 1
# 0 1 0 1 1
# 0 1 1 0 0
# 0 1 1 1 0
# 1 0 0 0 0
# 1 0 0 1 1
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 0 0 1
# 1 1 0 1 1
# 1 1 1 0 0
# 1 1 1 1 0



