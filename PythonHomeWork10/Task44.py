import random
import pandas as pd

# Ваш исходный код
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
one_hot_data = pd.DataFrame()
for i in data['whoAmI']:
    one_hot_data[i] = (data['whoAmI'] == i).astype(int)
print(one_hot_data)
one_hot_data.head()