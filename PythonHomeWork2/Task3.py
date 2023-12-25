# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("Введите число: "))
degree = 0
while n >= 2 ** degree:
    if 2 ** degree >= n:
        break
    print(2 ** degree)
    degree += 1
if 2 ** degree <= n:
    print(2 ** degree)