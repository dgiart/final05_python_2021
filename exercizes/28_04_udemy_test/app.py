from flask import Flask, request
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api, Resource

# from models import Book

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# Connects our Flask App to our Database

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://art:artem@localhost/udemy_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)
api = Api(app)
import models


class Employees(Resource):
    def get(self, name, birth, salary):
        employees = models.Employee.query.all()
        print('hop from rest')
        return str(len(employees))
        # return 'employees'

    def post(self, name, birth, salary):
        print('WTF')
        # posted_data = request.get_json()
        # name = posted_data['name']
        # birth = posted_data['birth']
        # salary = posted_data['salary']
        employee = models.Employee(name=name, birth=birth, salary=salary)
        db.session.add(employee)
        db.session.commit()


@app.route('/')
def hi():
    print('hop')
    return 'hi!'


api.add_resource(Employees, '/employees/<string:name>&<string:birth>&<string:salary>')

if __name__ == '__main__':
    app.run(debug=True)
# db.drop_all()
