"""3
Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def max_sum(a, b, c, d):
    return sum((a, b, c, d)) - min(a, b, c)
