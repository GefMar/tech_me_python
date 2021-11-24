import datetime

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)


__all__ = (
    'Base',
    "PromoProduct",
)

Base = declarative_base()


class PromoProduct(Base):
    __tablename__ = 'promo_product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    create_date = Column(DateTime, default=datetime.datetime.utcnow)
    url = Column(String, unique=True, nullable=False)
    title = Column(String, unique=False, nullable=True)
