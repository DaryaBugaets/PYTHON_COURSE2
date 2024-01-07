# Задача №63. 
# 1. Изобразите отношение households к population с помощью точечного графика
# 2. Визуализировать longitude по отношения к median_house_value, используя линейный график
# 3. Представить гистограмму по housing_median_age
# 4. Изобразить гистограмму по median_house_value с оттенком housing_median_age

# 1. Изобразите отношение households к population с помощью точечного графика
# from pandas import read_csv
# data = read_csv('D:\IT\PYTHON_COURSE2\PYTHON_COURSE2\california_housing_test.csv')

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('D:\IT\PYTHON_COURSE2\PYTHON_COURSE2\california_housing_test.csv')
## sns.scatterplot(data=df, x='households', y='population', hue='median_house_value')
# sns.scatterplot(data=df, x='households', y='population')

# 2. Визуализировать longitude по отношения к median_house_value, используя линейный график
# sns.relplot(x='longitude', y='median_house_value', kind='line', data=df)

# 3. Представить гистограмму по housing_median_age
# sns.histplot(data=df, x='housing_median_age')

# 4. Изобразить гистограмму по median_house_value с оттенком housing_median_age
sns.histplot(data=df, x='median_house_value', hue='housing_median_age')

plt.show()