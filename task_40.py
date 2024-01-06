# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке
# sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)
# (Дан файл california_housing_train.csv. Определить среднюю стоимость дома , 
# где количество людей от 0 до 500 (population) и сохранить ее в переменную avg.
# Используйте модуль pandas.)

from pandas import read_csv
data = read_csv('D:\IT\PYTHON_COURSE2\PYTHON_COURSE2\california_housing_test.csv')
avg = (data['population']>=0) & (data['population']<=500) 
print(avg)


# auto

# import pandas as pd
# data = pd.read_csv("california_housing_train.csv")
# filtered_data = data[(data['population'] >= 0) & (data['population'] <= 500)]
# avg = filtered_data['median_house_value'].mean()