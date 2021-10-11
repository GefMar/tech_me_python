#  Сначала импорт пакетов стандартной комплектации
# import time
from time import time
import datetime
import random


# Импорт пакетов установленных через pip

# Импорт пакетов написанных вами

# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
# print(time())
# some_date = "09.12.2054"
# a = datetime.datetime.strptime(some_date, "%d.%m.%Y")
# now = datetime.datetime.now()
# now.strftime("%H:%M -- %d.%m.%Y")

# my_list = ['cat', "dog", "rat"]
# 
# for animal in my_list:
#     print(animal)
#     print("-" * 10)

"пройти по диапозону чисел от 1 до 100 включительно"
# 
# n = 1
# stop = 100
# while n <= stop:
#     print(n)
#     n += 1

# for n in range(0, 101, 2):
#     print(n)
# 
some_list = ("dog", "cat", "rat")
some_list2 = ("home", "office", "street")

# matrix_1 = [[1, 2, 3, 4], [12, 13, 14, 15], [21, 22, 23, 24], [31, 32, 33, 34]]
# matrix_2 = [[100, 200, 300, 400], [120, 139, 149, 159], [219, 229, 239, 249], [319, 329, 339, 349]]
# 
# matrix_sum = []
# 
# for rows in zip(matrix_1, matrix_2):
#     row = []
#     for elements in zip(*rows):
#         row.append(sum(elements))
#     matrix_sum.append(row)
# 
# print(matrix_sum)

# some_dict = dict(zip(some_list, some_list2))
# 
# for itm in some_dict.items():
#     print(itm)


words = ['hel', 'low', 'frog', 'hello', 'lohel', 'hlelo', 'leh', ]
"""
[['hel', 'leh'], ['low'], ['frog'], ['hello', 'lohel', 'hlelo']]
"""
# groups = {}
# for word in words:
#     sort_word = tuple(sorted(word))
#     if sort_word in groups:
#         groups[sort_word].append(word)
#     else:
#         groups[sort_word] = [word]
# 
# print(list(groups.values()))

# 
# some = (1, 2, 3, 4, 5)
# 
# result = 0
# for itm in some:
#     result += itm
# 
# example_list = [1, 2, 3, [4, 5, 6, [7, [1, 2, 3], 8], 9], 10, [11], [[[12, [13]]]]]
# """
# [1, 2, 3, 4, 5, 6, 7, 1, 2, 3......]
# """
# result = []
# while example_list:
#     itm = example_list.pop(0)
#     print("*"*20)
#     print(example_list)
#     print(itm)
#     if isinstance(itm, list):
#         itm.extend(example_list)
#         example_list = itm
#     else:
#         result.append(itm)
# 
# print(result)
# 
# 
# user_input = input("введите слова через пробел\n>>>")
# user_words = user_input.split(" ")
# max_word_len = 10
# 
# for idx, word in enumerate(user_words, start=1):
#     print(f"{idx}: {word[:max_word_len]}")
#     # idx += 1
