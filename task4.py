"""
    ---Task 4---
Создайте функцию генератор чисел Фибоначчи
"""


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib_gen = fibonacci_generator()

for _ in range(10):
    fib_num = next(fib_gen)
    print(fib_num)
