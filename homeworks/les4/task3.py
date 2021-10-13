
"""
Имеется 2 кортежа с координатами Королева и Пешки на шахматной доске
Определить Бьет ли Ферзь пешку
координаты хранятся (x, y)
"""
queen = (2, 6)
pawn = (1, 7)
result = queen[0] == pawn[0] or queen[1] == pawn[1] or (abs(queen[1] - pawn[1]) == abs(queen[0] - pawn[0]))

print(result)
