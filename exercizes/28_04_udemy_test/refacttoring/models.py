from app import db


class Book(db.Model):
    # __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    author = db.Column(db.String(250), nullable=False)
    published = db.Column(db.Integer)
    cost = db.Column(db.Integer)

    # genre = db.Column(db.String(250))

    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre


class Employee(db.Model):
    eid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    birth = db.Column(db.Integer)
    salary = db.Column(db.String(250), nullable=False)

    def __init__(self, name, birth, salary):
        self.name = name
        self.birth = birth
        self.salary = salary

    def __repr__(self):
        return f'name: {self.name}, id={self.eid}'

    def json(self):
        return {'id': self.eid, 'name': self.name}


class test(db.Model):
    eid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
