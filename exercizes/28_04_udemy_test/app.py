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
    @staticmethod
    def get(name, birth, salary):
        employee = models.Employee.query.filter_by(name=name).first()
        if employee:
            print(f'hop from rest get {name}')
            return employee.__repr__()
        else:
            return f'There is not emloyee with name {name}'

    @staticmethod
    def post(name, birth, salary):
        print('WTF')
        employee = models.Employee(name=name, birth=birth, salary=salary)
        db.session.add(employee)
        db.session.commit()

    @staticmethod
    def delete(name, birth, salary):
        employee = models.Employee.query.filter_by(name=name).first()
        if employee:
            print(f'hop from rest get {name}')
            db.session.delete(employee)
            db.session.commite()
            return f'employee {name} is deleted'
        else:
            return f'There is not employee with name {name}'


@app.route('/')
def hi():
    print('hop')
    return 'hi!'


@app.route('/employees')
def get_all():
    employees = models.Employee.query.all()
    return {'emloyees': [employee.json() for employee in employees]}


@app.route('/employees/<string:name>')
def get(name):
    employee = models.Employee.query.filter_by(name=name).first()
    if employee:
        print(f'hop from rest get {name}')
        return employee.__repr__()
    else:
        return f'There is not emloyee with name {name}'


@app.route('/employees/salary')
def salary():
    employees = models.Employee.query.all()
    total = 0
    for employee in employees:
        total += float(employee.salary)
    average = total / (len(employees))
    return f'total = {total}, average = {average}'


api.add_resource(Employees, '/employees/<string:name>&<string:birth>&<string:salary>')

if __name__ == '__main__':
    app.run(debug=True)
# db.drop_all()
