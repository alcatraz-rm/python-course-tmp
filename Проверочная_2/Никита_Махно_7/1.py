"""
Правильно

1. Результат функции format уже имеет строковый тип, не нужно еще раз преобразовывать его в строку;
2. Можно не ставить скобки в if, если условия простые.
"""


for x in range(1, 1000):
    bin_num = x
    bin_num = format(bin_num, 'b')
    bin_num = str(bin_num)
    one_counter = bin_num.count("1")
    if (one_counter % 2 == 0):
        bin_num += "0"
    else:
        bin_num += "1"
    bin_num += str(int(bin_num) % 2)
    bin_num = int(bin_num, 2)
    if (bin_num > 180):
        print(bin_num)
        break
#answer 184