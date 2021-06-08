from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api


app = Flask(__name__)
# Connects our Flask App to our Database

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://art:artem@localhost/departments'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecretkey'

db = SQLAlchemy(app)
import models.models
Migrate(app, db)
api = Api(app)
# dept_api = Api(departments_blueprint)
db.create_all()
print(f'IMPORT db={db} and app={app}')
