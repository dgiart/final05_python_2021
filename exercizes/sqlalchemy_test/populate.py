from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# импортируем классы Book и Base из файла database_setup.py
from database_setup import Book, Base, engine
import mysql.connector

import alembic
# engine = create_engine('mysql+mysqlconnector://art:artem@localhost/books')
# Свяжим engine с метаданными класса Base,
# чтобы декларативы могли получить доступ через экземпляр DBSession
# Base.metadata.bind = engine

# DBSession = sessionmaker(bind=engine)
# Экземпляр DBSession() отвечает за все обращения к базе данных
# и представляет «промежуточную зону» для всех объектов,
# загруженных в объект сессии базы данных.
# session = DBSession()
def del_book(title):
    bookToDelete = session.query(Book).filter_by(title=title).one()
    session.delete(bookToDelete)
    session.commit()


def add_book(title='title', author='author', genre='genre'): #, cost = 10):
    book = Book(title=title, author=author, genre=genre)#, cost=cost)
    session.add(book)
    session.commit()


if __name__ == '__main__':
    # engine = create_engine('mysql+mysqlconnector://art:artem@localhost/books')
    # Свяжим engine с метаданными класса Base,
    # чтобы декларативы могли получить доступ через экземпляр DBSession
    # Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    # Экземпляр DBSession() отвечает за все обращения к базе данных
    # и представляет «промежуточную зону» для всех объектов,
    # загруженных в объект сессии базы данных.
    session = DBSession()
    # bookOne = Book(title="Pure c222", author="Art Baiden", genre="computer leterature")
    # session.add(bookOne)
    # session.commit()
    add_book()
    # del_book("Pure c222")
