def func(n1, n2):
    a, b = 0, 1
    while a <= n2:
        if a >= n1:
            yield a
        a, b = b, a + b

res = func(5, 50)
fib_list = list(res)

if fib_list:
    print(", ".join(map(str, fib_list)))
else:
    print("В заданном диапазоне нет чисел Фибоначчи")