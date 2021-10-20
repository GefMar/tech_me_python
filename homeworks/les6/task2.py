"""2
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
"""


def no_repeat(iter_object):
    for itm in iter_object:
        if iter_object.count(itm) == 1:
            yield itm


def no_repeat_filter(iter_object):
    # for itm in filter(lambda x: iter_object.count(x) == 1, iter_object):
    #     yield itm

    yield from filter(lambda x: iter_object.count(x) == 1, iter_object)


data = [1, 2, 3, 1, 4, 2, 6, 12, 4]
result = list(no_repeat(data))

result_2 = list(no_repeat_filter(data))

print(result)
print(result_2)
