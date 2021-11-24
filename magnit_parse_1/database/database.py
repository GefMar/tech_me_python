from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from . import models


class DataBase:

    def __init__(self, db_url):
        engine = create_engine(db_url)
        models.Base.metadata.create_all(bind=engine)
        self.maker = sessionmaker(bind=engine)

    def save_promo_products(self, *products_dicts):
        products = [models.PromoProduct(**itm) for itm in products_dicts]
        session = self.maker()
        session.add_all(products)
        try:
            session.commit()
        except Exception as exc:
            session.rollback()
        finally:
            session.close()
