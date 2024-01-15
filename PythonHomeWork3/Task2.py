# Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.

list_1 = [1, 4, 3, 7, 8, 9, 2]
res = 0
multiply = 0
k = int(input("Введите число: "))
difference = k
for i in list_1:
    if k - i < 0:
        multiply = (k - i) * -1
    if multiply < difference:
        difference = k - i
        res = i
    elif k == i:
        res = i
        break
print(res)