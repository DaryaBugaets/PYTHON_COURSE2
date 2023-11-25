# Задача №19. Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3  Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения списка или список задан изначально.

# import random
# N=int(input('Введите количество чисел: '))
# k=int(input('Введите сдвиг: '))
# list_1=[]
# for i in range(N):
#     list_1.append(random.randint(1, 20))
# print(list_1)

# for i in range(k):
#     list_1.append(list_1[0])
#     list_1.pop(0)
# print(list_1)

list_1 = [1, 2, 3, 4, 5] 
k = 3
print(list_1)
for i in range(k):  #итерация на к
    list_1.append(list_1[0]) #добавление элементов
    list_1.pop(0)   #удаление элементов, начиная с первого
print(list_1)
# +
# через срез
list_1 = [1, 2, 3, 4, 5] 
new_lst=list_1[k:]+list_1[:k]
print(new_lst)


list_1 = [1, 2, 3, 4, 5]
for i in range(k-1):
    el=list_1.pop()  # удалим  и вернем последний элемент массива, el-элемент
    list_1.insert(0, el)
print(list_1)



