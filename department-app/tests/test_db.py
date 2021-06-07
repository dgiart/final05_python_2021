import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_restful import Api
from service.database_funcs import Database


if __name__ == '__main__':
    b = Database()
    b.drop_base('db_to_test', 'art', 'artem', 'localhost')
    # b.create_base('db_to_test', 'art', 'artem', 'localhost')


@pytest.fixture
def db_to_test():
    b = Database()
    b.create_base('db_to_test', 'art', 'artem', 'localhost')
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://art:artem@localhost/db_to_test'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    # import models.models
    Migrate(app, db)
    # api = Api(app)
    # dept_api = Api(departments_blueprint)
    db.create_all()
    yield db
    b.drop_base('db_to_test', 'art', 'artem', 'localhost')

def test_db(db_to_test):
    print(db_to_test)
