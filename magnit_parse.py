from magnit_parse_1 import MagnitParser
from magnit_parse_1.database import database


if __name__ == '__main__':
    database = database.DataBase("sqlite:///magnit.db")
    parser = MagnitParser("https://magnit.ru/promo/", database)
    parser.run()
