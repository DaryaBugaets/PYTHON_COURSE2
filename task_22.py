"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.
11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12
"""
# from random import randint
# n_set = set(randint(1, 100) for i in range(int(input('Введите кол-во элементов первого множества: '))))
# m_set = set(randint(1, 100) for i in range(int(input('Введите кол-во элементов второго множества: '))))
# print(n_set)
# print(m_set)
# s_set = sorted(n_set.intersection(m_set))
# print(*s_set)

# import random
# n = (int(input("Введите кол-во элементов первого множества: ")))
# m = (int(input("Введите кол-во элементов второго множества: ")))
# data1= [random.randint(1, n) for i in range(n)]
# print(data1)
# data2= [random.randint(1, m) for i in range(m)]
# print(data2)

# n=int(input("Введите кол-во элементов первого множества: "))
# m=int(input("Введите кол-во элементов второго множества: "))


# n=(int(input("Введите число N элементов: ")))
# num_list_1=[]
# for i in range(n):
#     num = int(input("Введите num "))
#     num_list_1.append(num)
# print(num_list_1)


# m=(int(input("Введите число M элементов: ")))
# num_list_2 = []
# for i in range(m):
#     num = int(input("Введите num "))
#     num_list_2.append(num)
# print(num_list_2)


# num_list3 = num_list_1+num_list_2

# print(num_list3)
# for i in set(num_list3):
#     if num_list3.count(i) > 1:
#         print(i, end=' ')


# var1 = '5 4' 
# var2 = '1 3 5 7 9' 
# var3 = '2 3 4 5' 

# num_set2=set(var2)
# num_set3 = set(var3)
# num= sorted (num_set2.intersection(num_set3))
# print(*num)


var1 = '5 4' 
var2 = '1 3 5 7 9' 
var3 = '2 3 4 5' 

mol = [int(x) for x in var1.split()]
n = mol[0]
m = mol[1]
set_1 = set()
set_2 = set()
list_1 = list()
a = [int(x) for x in var2.split()]
k = set(a)
for i in k:
   set_1.add(i)
b = [int(x) for x in var3.split()]
k1 = set(b)
for i in k1:
   set_2.add(i)
lok = set_1 & set_2
kool = list(lok)
kool.sort()
for i in kool:
   print(i, end=' ')


