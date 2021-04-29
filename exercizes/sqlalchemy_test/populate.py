from sqlalchemy.orm import sessionmaker
# from database_setup import engine, Book
from models import Book
from sqlalchemy import create_engine


engine = create_engine('mysql+mysqlconnector://art:artem@localhost/udemy_test')

DBSession = sessionmaker(bind=engine)
session = DBSession()


def del_book(title):
    bookToDelete = session.query(Book).filter_by(title=title).one()
    session.delete(bookToDelete)
    session.commit()


def add_book(title='title', author='author', genre='genre'): #, cost = 10):
    book = Book(title=title, author=author, genre=genre)#, cost=cost)
    session.add(book)
    session.commit()


if __name__ == '__main__':

    # bookOne = Book(title="Math", author="Eiler", genre="scientific leterature")
    # session.add(bookOne)
    # session.commit()
    add_book(title="Привет, Мир!", author="Van", genre="Python")
    # del_book("Pure c222")
