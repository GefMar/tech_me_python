""" 1
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
"""


def some_search(iter_object):
    previous = -float("inf")
    for itm in iter_object:
        if itm > previous:
            yield itm
        previous = itm


result = list(some_search([1, 3, 2, 3, -5, 6, 19, 8, 9]))
print(result)
