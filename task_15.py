# Задача №15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9 Output: 1 9

# lst= list(map(int, input("Введите массу арбузов, через пробел: ").split(" ")))
# print(min(lst), max(lst))

# n=int(input("Введите количество арбузов: "))
# x=int(input("введите массу арбуза: "))
# max_massa, min_massa=x, x
# for i in range(n-1):
#     x=int(input("введите массу арбуза: "))
#     if max_massa<x:
#         max_massa=x
#     elif min_massa>x:
#         min_massa=x
# print(min_massa, max_massa)     

from random import randint
n=int(input("Введите количество арбузов: "))
watermelons=[]
for i in range(n):
    watermelons.append(randint(1,20))   #добаляет элемент в конец списка
print(watermelons)
print(f'Минимальный арбуз {min(watermelons)} кг')
print(f'Максимальный арбуз {max(watermelons)} кг')

# ошибка
# n=int(input("Введите количество арбузов: "))
# max_massa=0
# min_massa=0
# for i in range(n):
#     x=int(input("введите массу арбуза: "))
#     if max_massa<x:
#          max_massa=x
#     if min_massa>x:
#          min_massa=x
# print(min_massa, max_massa)     
