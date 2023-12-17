# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Если строк меньше двух, выдайте текст: ОШИБКА! Размерности таблицы должны 
# быть больше 2! Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.
# Ввод: print_operation_table(lambda x, y: x * y) 
# Вывод:
#  1  2  3  4  5  6
#  2  4  6  8  10 12
#  3  6  9  12 15 18
#  4  8  12 16 20 24
#  5  10 15 20 25 30
#  6  12 18 24 30 36

# def print_operation_table(operation, num_rows=6, num_columns=6):
#     result = []
#     if num_rows < 2 or num_columns < 2:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!')
#     else:
#         print(''.join([str(i) for i in range(1, num_columns + 1)]))
#         for i in range(2, num_rows + 1):
#             result.append(i)
#             for j in range(2, num_columns + 1):
#                 if j != num_columns:
#                     result.append(f'{operation(i, j)}')
#                 else:
#                     result.append(operation(i, j))
#             result.append('\n')
#         print("".join([str(i) for i in result[:len(result)-1]]))
# print_operation_table(lambda x, y: x * y, 3, 3)

   
# def print_operation_table(operation, num_rows=4, num_columns=6):

#     for row in range(1, num_rows+1):  # цикл по строкам таблицы

#         for column in range(1, num_columns+1):  # цикл по столбцам таблицы

#             result = operation(row, column)  # вызов функции operation

#             print(result, end=' ')  # печать результата с табуляцией

#         print()  # печать символа перевода строки после каждой строки таблицы 
# print_operation_table(lambda x, y: x * y, 4, 8)   

# Функция print_operation_table будет состоять из двух вложенных циклов: 
# первый цикл будет проходить по строкам таблицы, а второй цикл - по столбцам. 
# В каждой итерации цикла будет вызываться функция operation с передачей номера 
# строки и столбца, и результат этой функции будет печататься.
# В данном коде используются два вложенных цикла с использованием функции `range()`. 
# При вызове функции `range()` указывается диапазон значений от 1 до `num_rows` + 1 
# для цикла по строкам и от 1 до `num_columns` + 1 для цикла по столбцам. 
# Это сделано для того, чтобы порядковые номера строк и столбцов начинались с единицы 
# (как на листе бумаги), а не с нуля. 
# В каждой итерации цикла вызывается функция `operation` с передачей номера строки и 
# столбца в качестве аргументов. Результат работы этой функции сохраняется в переменную `result`. 
# Затем результат печатается с помощью функции `print()`, а после каждой строки таблицы 
# выводится символ перевода строки с помощью второго вызова `print()` без аргументов.
# Таким образом, функция `print_operation_table` будет печатать таблицу, 
# в которой каждый элемент вычисляется с помощью функции `operation` в зависимости от номера строки и столбца.


# def print_operation_table(operation, num_rows=6, num_columns=6):
#     def calculate_element(row, column):
#         return operation(row, column)
#     for i in range(1, num_rows+1):
#         for j in range(1, num_columns+1):
#             print(calculate_element(i, j), end=" ")
#         print()
# print_operation_table(lambda x, y: x * y, 3, 3)

def print_operation_table(operation, num_rows=6, num_columns=6):
    if num_rows < 2 or num_columns < 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        print(' '.join([str(i) for i in range(1, num_columns + 1)]))
        for i in range(2, num_rows + 1):
            row = [str(i)]
            for j in range(2, num_columns + 1):
                row.append(f'{operation(i, j)}')
            print(' '.join(row))
print_operation_table(lambda x, y: x * y, 8, 3)


