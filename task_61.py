# Задача №61. 
# 1. Определить какое максимальное и минимальное значение median_house_value
# 2. Показать максимальное median_house_value, где median_income = 3.1250
# 3. Узнать какая максимальная population в зоне минимального значения median_house_value

from pandas import read_csv
data = read_csv('D:\IT\PYTHON_COURSE2\PYTHON_COURSE2\california_housing_test.csv')

# 1. Определить какое максимальное и минимальное значение median_house_value
print(f"{data['median_house_value'].max()}, {data['median_house_value'].min()}")

# 2. Показать максимальное median_house_value, где median_income = 3.1250
print(data[data['median_income'] == 3.1250]['median_house_value'].max())

# 3. Узнать какая максимальная population в зоне минимального значения median_house_value
res = data[data['median_house_value'] == data['median_house_value'].min()]['population'].max()
print(res)