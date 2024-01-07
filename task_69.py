# Задача №69. 
# Изобразить гистограмму по flipper_length_mm с оттенком height_group. Сделать анализ

from pandas import read_csv
# import from seaborn as sns
# import histplot
from seaborn import histplot
# import matplotlib.pyplot as plt
from matplotlib.pyplot import show

penguins = read_csv('penguins.csv')

histplot(penguins, x='flipper_length_mm', hue='height_group')

show()