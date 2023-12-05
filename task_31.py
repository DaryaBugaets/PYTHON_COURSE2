# Задача №31. Последовательностью Фибоначчи называется последовательность чисел a0 , a1 , ..., an , ..., где
# a0  = 0, a1  = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7 Output: 21 Задание необходимо решать через рекурсию

# 1 2 3 5 8 13 21

def fibonacci(n):
    if n in [1, 2]:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
n=7
print(fibonacci(n))



fib1, fib2 = 0, 1  
for i in range (0, n):
    fib1, fib2 = fib2, fib1+fib2
print(fib2)
