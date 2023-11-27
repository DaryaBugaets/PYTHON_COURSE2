'''''
Задача №21. Напишите программу для печати всех уникальных значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, 
{" V ":" S009 "}, {" VIII ":" S007 "}]  Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
Примечание: Список словарей задан изначально. Пользователь его не вводит
'''''

lst_obj= [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, 
{" V ":" S009 "}, {" VIII ":" S007 "}]
my_set=set() #взять все значения в словавре и отсечь дубли, поэтому начинаем с объявления множества(и у нас-snake case(нижнее подчеркивание))


# традиционный итератор с функцией add, для множества
for el in lst_obj: #нам надо обойти элементы списка, берем по одному словарю и проваливаемся в цикл, и их обходим
   for item in el.values(): #сначала нужно добраться до значений словаря
        my_set.add(item)   #далее item положить в set, добавили элементы значений из словаря
print(my_set) #печатаются значения


# вариант, через включение для множества(множественное включение)-set comprehension(sc)

my_set=set(item for el in lst_obj for item in el.values())#все делаем во множестве, сначала внешний цикл, затем цикл вложенный
# перед внешним for размещаем - просто, сам элемент