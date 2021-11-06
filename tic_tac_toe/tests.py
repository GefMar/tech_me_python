from tic_tac_toe.board import get_board, board_match


def board_test():
    for size in range(3, 6):
        board = get_board(size)
        assert len(board) == size, "Неверная размерность доски"
        assert len(min(board)) == len(max(board)), "Неравная длина строк доски"
        assert len(min(board)) == size, "Неверная размерность строк доски"
        assert set(sum(board, [])) == {0, }, "Неверное заполнение доски"


def test_board_match():
    matrix_tests = (
        (([1, 1, 1],
          [0, 0, 0],
          [0, 0, 0]), True),

        (([0, 0, 0],
          [1, 1, 1],
          [0, 0, 0]), True),

        (([0, 0, 0],
          [0, 0, 0],
          [2, 2, 2]), True),

        (([0, 1, 2],
          [0, 0, 1],
          [1, 1, 2]), False),

        (([1, 0, 0],
          [1, 0, 0],
          [1, 0, 0]), True),

        (([0, 1, 0],
          [0, 1, 0],
          [0, 1, 0]), True),

        (([0, 0, 2],
          [0, 0, 2],
          [0, 0, 2]), True),
        (([2, 1, 2],
          [0, 1, 2],
          [0, 0, 1]), False),
        (([1, 1, 2],
          [0, 1, 2],
          [0, 0, 1]), True),
        (([2, 1, 1],
          [0, 1, 2],
          [1, 0, 1]), True),
    )

    for test in matrix_tests:
        assert board_match(test[0]) is test[1], test[0]


if __name__ == '__main__':
    board_test()
    test_board_match()
