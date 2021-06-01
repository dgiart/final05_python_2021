from flask import Blueprint, jsonify, request
from flask_restful import Resource, Api
from service.crud import add_employee, get_employees, get_employee, del_employee, put_employee
from models.models import employee_keys
from rest.checkers import employee_check

rest_employees_blueprint = Blueprint('employees', __name__)
empl_api = Api(rest_employees_blueprint)


class Employees(Resource):
    def post(self):
        data = request.json
        birthday = employee_check(data, employee_keys)
        print(f'birthday: {birthday}')
        if not birthday:
            return 'Bad Request', 400
        name = data.get('name')
        salary = data.get('salary')
        id_empl_dept = data.get('id_empl_dept')
        item_id = add_employee(name, salary, birthday, id_empl_dept)
        employee = {'id': item_id, 'name': name}
        resp = jsonify(employee)
        resp.status_code = 201
        # resp = None
        return resp

    def get(self):
        employees = get_employees()
        resp = jsonify(employees)
        resp.status_code = 200
        return resp


class EmployeeItem(Resource):
    def get(self, id_empl):
        """
        Method get employee id from url and gets corresponding employee
        :param id_empl: employee id
        :return: if success -> employee info, if not -> message': employee with id does not exist
        """
        employee = get_employee(id_empl)
        resp = jsonify(employee)
        resp.status_code = 200
        return resp

    def delete(self, id_empl):
        """
        Method delete employee id from url and deletes corresponding employee
        :param id_empl:
        :return: if success -> employee id, if not -> message': employee with id does not exist
        """
        deleted = del_employee(id_empl)
        if deleted:
            resp = jsonify({'message': f'employee #{id_empl} deleted'})
            resp.status_code = 200
            return resp
        else:
            resp = jsonify({'message': f'employee #{id_empl} does not exist'})
            return resp

    def put(self, id_empl):
        data = request.json
        birthday = employee_check(data, employee_keys)
        print(f'birthday: {birthday}')
        if not birthday:
            return 'Bad Request', 400
        name = data.get('name')
        salary = data.get('salary')
        id_empl_dept = data.get('id_empl_dept')
        item_id = put_employee(id_empl, name, salary, birthday, id_empl_dept)
        employee = {'id': item_id, 'name': name}
        resp = jsonify(employee)
        resp.status_code = 201
        # resp = None
        return resp


empl_api.add_resource(Employees, '/')
empl_api.add_resource(EmployeeItem, '/<int:id_empl>')
