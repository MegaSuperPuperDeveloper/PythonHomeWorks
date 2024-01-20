# Дан файл california_housing_train.csv. Определить среднюю стоимость дома , где количество людей от
# 0 до 500 (population) и сохранить ее в переменную avg. Используйте модуль pandas.

from pandas import read_csv
data = read_csv("california_housing_test.csv")

count = 0
sum = 0
avg = data[(data["population"] <= 500) & (data["population"] >= 0)]["median_house_value"]
for i in avg:
    sum += i
    count += 1
avg = sum / count
print(avg)