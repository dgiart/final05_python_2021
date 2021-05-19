from flask_restful import Resource
from flask import jsonify, request
from app import app, db, api
import models


class Employees(Resource):
    @staticmethod
    def get(name, birth, salary):
        employee = models.Employee.query.filter_by(name=name).first()
        if employee:
            print(f'hop from rest get {name}')
            return jsonify(employee.__repr__())
        else:
            return f'There is not emloyee with name {name}'

    @staticmethod
    def post(name, birth, salary):
        print('WTF')
        employee = models.Employee(name=name, birth=birth, salary=salary)
        db.session.add(employee)
        db.session.commit()
        print(f'New employee: {employee.__repr__()}')
        to_return = {
            'new emloyee':
            employee.__repr__()
        }
        return to_return

    @staticmethod
    def delete(name, birth, salary):
        employee = models.Employee.query.filter_by(name=name).first()
        if employee:
            print(f'hop from rest DEL {name}')
            db.session.delete(employee)
            db.session.commit()
            return f'employee {name} is deleted'
        else:
            return f'There is not employee with name {name}'


@app.route('/', methods=['POST', 'GET'])
def hi():
    if request.method == 'GET':
        print('hop')
        l = [True, 1, 2, 3]
        return jsonify(l)
        # return {'hi!': 'Hop! Hop!'}
    if request.method == 'POST':

        req = request.get_json()
        print(f'REQ: {req}')
        r = (request.get_data())
        print(r)
        print(f'POST to INDEX: {req}')
        # return jsonify(r)
        return jsonify(req)


@app.route('/employees')
def get_all():
    print('view.py')
    employees = models.Employee.query.all()
    return jsonify({'emloyees': [employee.json() for employee in employees]})


@app.route('/employees/<string:name>')
def get(name):
    employee = models.Employee.query.filter_by(name=name).first()
    if employee:
        print(f'hop from rest get {name}')
        return jsonify(employee.__repr__())
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
