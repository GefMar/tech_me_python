import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Boolean,
    DateTime,
    Table,
)


Base = declarative_base()

_child_section = Table(
    "child_section",
    Base.metadata,
    Column("child_id", Integer, ForeignKey("child.id")),
    Column("section_id", Integer, ForeignKey("section.id"))
)


class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), unique=False)
    b_date = Column(DateTime, unique=False)


class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), unique=False)
    b_date = Column(DateTime, unique=False)
    parent_id = Column(Integer, ForeignKey("parent.id"), nullable=True)
    parent = relationship(Parent, backref='children')
    sections = relationship("Section", secondary=_child_section, backref='children')

    @property
    def age(self):
        return datetime.datetime.now().year - self.b_date.year


class Section(Base):
    __tablename__ = 'section'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), unique=True)
