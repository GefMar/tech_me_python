# Дано 2 целых числа, написать алгоритм поиска наибольшего общего делителя

a = 24
b = 9

tmp_a = a
tmp_b = b
while tmp_a and tmp_b:
    # if tmp_a < tmp_b:
    #     tmp_a, tmp_b = tmp_b, tmp_a
    # else:
    #     tmp_a, tmp_b = tmp_a, tmp_b
    # tmp_a, tmp_b = (tmp_b, tmp_a) if tmp_a < tmp_b else (tmp_a, tmp_b)
    tmp_a %= tmp_b
else:
    result = tmp_a + tmp_b

print(result)
