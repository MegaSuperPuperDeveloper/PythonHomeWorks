# Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.

list_1 = [2, 4, 1, 6, 8, 2, 9, 3, 2, 5]
res = 0
multiply = 0
k = int(input("Введите число: "))
difference = k
for i in list_1:
    if k - i < 0:
        multiply = (k - i) * -1
    else:
        multiply = k - i
    if multiply < difference:
        difference = multiply
        res = i
    elif k == i:
        res = i
        break
print(res)