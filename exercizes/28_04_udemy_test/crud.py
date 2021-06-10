from app_old import db
from models import Book, Employee
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