# Задача №59.
# 1. Проверить есть ли в файле пустые значения
# 2. Показать median_house_value где median_income < 2
# 3. Показать данные в первых 2 столбцах
# 4. Выбрать данные где housing_median_age < 20 и median_house_value > 70000

from pandas import read_csv

# data=read_csv('california_housing_test.csv')
data = read_csv('D:\IT\PYTHON_COURSE2\PYTHON_COURSE2\california_housing_test.csv')

# # 1. Проверить есть ли в файле пустые значения
# # print(data.isnull().sum())
# # 2. Показать median_house_value где median_income < 2
# # res=data[data['median_income'] < 2]['median_house_value']
# # print(res)
# # 3. Показать данные в первых 2 столбцах
# # res=data[['longitude', 'latitude']]
# # print(res)
# # res=data.iloc
# # print(res)
# # 4. Выбрать данные где housing_median_age < 20 и median_house_value > 70000
res = data[(data['housing_median_age'] < 20) & (data['median_house_value'] > 70000)]
print(res)