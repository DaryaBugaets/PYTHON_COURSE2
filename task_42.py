# Задача 42: Узнать какая максимальная households в зоне минимального значения population

from pandas import read_csv
data = read_csv('D:\IT\PYTHON_COURSE2\PYTHON_COURSE2\california_housing_test.csv')
max_households_in_min_population=data[data['population'] == data['population'].min()]['households'].max()
print(max_households_in_min_population)


# auto

# import pandas as pd
# df = pd.read_csv("california_housing_train.csv")
# min_population = df['population'].min()
# max_households_in_min_population = df[df['population'] == min_population]['households'].max()

