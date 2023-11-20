# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0      2

# n=int(input('Введите количество монеток: '))
# reshka=gerb=0
# for i in range(n):
#     a=int(input('решка(1) или герб(0)'))
#     if a==1:
#         reshka+=1
#     else:
#         gerb+=1
# if reshka>gerb:
#     output=gerb
# else:
#     output=reshka
# print(f'Минимальное количество монет, которое нужно перевернуть{output}')

# coins = [0, 1, 0, 1, 1, 0]
# gerb=0
# reshka=0
# for i in coins:
#     if i == 0:
#         gerb+=1
#     else:
#         reshka+=1
# if reshka>gerb:
#     output=gerb
# else:
#     output=reshka
# print(f'Минимальное количество монет, которое нужно перевернуть {output}')


coins = [0, 1, 0, 1, 1, 0]
gerb=0
reshka=0
for i in coins:
    if i == 0:
        gerb+=1
    else:
        reshka+=1
if reshka>gerb:
    output=gerb
else:
    output=reshka
print(output)
        
