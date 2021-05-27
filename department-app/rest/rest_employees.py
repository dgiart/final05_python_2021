from flask import Blueprint, jsonify, request
from flask_restful import Resource, Api
from service.crud import add_employee, get_employees, get_employee

employees_blueprint = Blueprint('employees', __name__)
empl_api = Api(employees_blueprint)


class Employees(Resource):
    def post(self):
        name = request.json.get('name')
        salary = request.json.get('salary')
        birth = request.json.get('birth')
        item_id = add_employee(name, salary, birth)
        employee = {'id': item_id, 'name': name}
        resp = jsonify(employee)
        resp.status_code = 201
        return resp

    def get(self):
        employees = get_employees()
        resp = jsonify(employees)
        resp.status_code = 200
        return resp


class EmployeeItem(Resource):
    def get(self, id_empl):
        employee = get_employee(id_empl)
        resp = jsonify(employee)
        resp.status_code = 200
        return resp


empl_api.add_resource(Employees, '/')
empl_api.add_resource(EmployeeItem, '/<int:id_empl>')
