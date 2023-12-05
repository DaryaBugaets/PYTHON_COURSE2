# Задача №37.  Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы
# (даже для ввода и вывода). Input: 2 -> 3 4 Output: 4 3

def rev(n):
    if n > 0:
        num = int(input('число: '))
        rev(n-1)
        print(num, end=' ')
rev(2)

def reverse_print(lst):
    if len(lst) == 1:
        print(lst[0])
    else:
        print(lst[-1], end=' ')
        reverse_print(lst[:-1])
def input_list(length):
    if length == 1:
        return [int(input('число: '))]
    else:
        return input_list(length-1) + [int(input('число: '))]
    
l = int(input('введите длину списка: '))
lst = input_list(l)
print(lst)

reverse_print(lst)