from flask import Blueprint, jsonify, request
from flask_restful import Resource, Api
import logging
from datetime import datetime
from service.crud import add_employee, get_employees, get_employee, del_employee, put_employee
from models.models import employee_keys
from service.checkers import employee_check
logger = logging.getLogger('empl')

rest_employees_blueprint = Blueprint('employees', __name__)
empl_api = Api(rest_employees_blueprint)


class Employees(Resource):
    def post(self):
        data = request.json
        if not data:
            return 'Bad Request', 400
        try:
            birthday = employee_check(data, employee_keys)
        except TypeError as e:
            return 'Bad Request', 400
        name = data.get('name')
        salary = data.get('salary')
        id_empl_dept = data.get('id_empl_dept')
        item_id = add_employee(name, salary, birthday, id_empl_dept)
        employee = {'id': item_id, 'name': name}
        resp = jsonify(employee)
        resp.status_code = 201
        id_empl = add_employee(name, salary, birthday, id_empl_dept)
        log_msg = f'empl {id_empl_dept}, {name}, created : {datetime.now()}'
        logger.warning(log_msg)
        return resp

    def get(self):
        if not request.args:
            employees = get_employees()
        else:
            start_day = request.args.get('start_day')
            end_day = request.args.get('end_day')
            start_month = request.args.get('start_month')
            end_month = request.args.get('end_month')
            start_year = request.args.get('start_year')
            end_year = request.args.get('end_year')
            dates = start_year, start_month, start_day, end_year, end_month, end_day
            employees = get_employees(dates)
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
        """
        Method changes an employee with id
        :param id_empl: employee id
        :return: new employee
        """
        data = request.json
        print(f'data: {data}')
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
        return resp


empl_api.add_resource(Employees, '/')
empl_api.add_resource(EmployeeItem, '/<int:id_empl>')
