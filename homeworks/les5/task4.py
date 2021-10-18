"""4
Функция принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без операторов ** * (без умножения и без возведения в степень).
Можно и нужно использовать сложение (+) и возможно деление (/)
"""


def my_multip(x, y):
    result = 0
    for _ in range(y):
        result += x
    return result


def my_func(x: float, y: int):
    result = 1
    for _ in range(abs(y)):
        result = my_multip(result, x)
    return result if y > 0 else 1 / result


print(my_func(2, -3) == 2 ** -3)
