from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api


app = Flask(__name__)
# Connects our Flask App to our Database

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://art:artem@localhost/departments'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)
import models.models
api = Api(app)
