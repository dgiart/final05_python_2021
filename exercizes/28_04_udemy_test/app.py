from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from models import Book

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# Connects our Flask App to our Database

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://art:artem@localhost/udemy_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)

import models
#
# class Book(db.Model):
#     # __tablename__ = 'book'
#
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(250), nullable=False)
#     author = db.Column(db.String(250), nullable=False)
#     genre = db.Column(db.String(250))
#
#     def __init__(self, title, author, genre):
#         self.title = title
#         self.author = author
#         self.genre = genre


if __name__ == '__main__':
    db.create_all()
# db.drop_all()
