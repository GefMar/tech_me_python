from tic_tac_toe.board import get_board
from tic_tac_toe.game import game_init, game_cycle, game_end


def main():
    game_vars = game_init()
    end_result = True
    while end_result:
        result_game = game_cycle(**game_vars)
        end_result = game_end(*result_game)
        if end_result:
            game_vars["board"] = get_board(3)


if __name__ == '__main__':
    main()
