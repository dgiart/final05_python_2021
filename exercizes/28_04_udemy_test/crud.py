from app import db#, Book
from models import Book
db.create_all()
command = ''
while True:
    command = input('?')
    if command == 'stop':
        break

    title = input('title: ')
    author = input('author: ')
    genre = input('genre: ')
    book = Book(title, author, genre)
    db.session.add(book)
    db.session.commit()