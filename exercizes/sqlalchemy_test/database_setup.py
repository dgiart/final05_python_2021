from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

from models import Book


Base = declarative_base()



# class Book(Base):
#     __tablename__ = 'book'
#
#     id = Column(Integer, primary_key=True)
#     title = Column(String(250), nullable=False)
#     author = Column(String(250), nullable=False)
#     genre = Column(String(250))


engine = create_engine('mysql+mysqlconnector://art:artem@localhost/udemy_test')
Base.metadata.bind = engine
Base.metadata.create_all(engine)

# мы создаем класс Book наследуя его из класса Base.


# class Book(Base):
#     __tablename__ = 'book'
#
#     id = Column(Integer, primary_key=True)
#     title = Column(String(250), nullable=False)
#     author = Column(String(250), nullable=False)
#     genre = Column(String(250))
#     # cost = Column(Integer)


# создает экземпляр create_engine в конце файла
