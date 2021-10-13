"""
Дано 2 Матрицы 
Необходимо получить произведение данных матриц

"""

matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

result = []

for row in matrix_1:
    result_row = []
    for column in zip(*matrix_2):
        tmp_row = []
        for itm in zip(row, column):
            tmp_row.append(itm[0] * itm[1])
        result_row.append(sum(tmp_row))
    result.append(result_row)

print(result)
