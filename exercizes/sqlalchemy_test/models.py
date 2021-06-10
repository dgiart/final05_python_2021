from sqlalchemy import Column, ForeignKey, Integer, String
from database_setup import Base


# мы создаем класс Book наследуя его из класса Base.


class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    author = Column(String(250), nullable=False)
    genre = Column(String(250))
    # cost = Column(Integer)
