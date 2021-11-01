import datetime

SYMBOLS = ("X", "O")

COMP_NAMES = [
    "R2D2",
    "C3PO",
    "WALLE",
    "DALEK",
]

USER_TEMPLATE = (
    ("name", lambda *args, **kwargs: input("ВВЕДИТЕ ВАШЕ ИМЯ")),
    ("symbol", lambda symbol, *args, **kwargs: symbol),
    ("steps", lambda *args, **kwargs: list()),
    ("all_steps", lambda *args, **kwargs: set()),
    ("user_type", lambda user_type, *args, **kwargs: user_type),
)

LOG_FOLDER = "game_logs"

FILE_HANDLERS = {
    "GAME_NUM": "game_num_inc",
    "INIT_GAME": "game_init",
    "GAME_STEP": "game_log",
}

INIT_ROW_TEMPLATE = {
    "game_id": int,
    "mode": str,
    "x_user_name": str,
    "o_user_name": str,
    "date_start": datetime.datetime.fromisoformat,
}
GAME_LOG_TEMPLATE = ("game_id", "step_date", "user_name", "user_step")
