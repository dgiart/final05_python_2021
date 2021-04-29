from app import db


class Book(db.Model):
    # __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    author = db.Column(db.String(250), nullable=False)
    genre = db.Column(db.String(250))

    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
