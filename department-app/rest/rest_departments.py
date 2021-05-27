from flask import Blueprint, jsonify, request
from flask_restful import Resource, Api
from service.crud import add_department, get_departments, get_department, del_department
from rest.checkers import department_check

departments_blueprint = Blueprint('departments', __name__)
dept_api = Api(departments_blueprint)


class Departments(Resource):
    def post(self):
        data = request.get_json()
        if not department_check(data):
            return 'Bad Request', 400
        title = data.get('title')
        item_id = add_department(title)
        department = {'title': title, 'id': item_id}
        resp = jsonify(department)
        resp.status_code = 201
        return resp

    def get(self):
        departments = get_departments()
        resp = jsonify(departments)
        resp.status_code = 200
        return resp


class DepartmentItem(Resource):
    def get(self, dept_id):
        department = get_department(dept_id)
        if department:
            print(f"get department: {dept_id}")
            resp = jsonify(department)
            resp.status_code = 200
            return resp
        else:
            resp = jsonify({'message': f'department #{dept_id} does not exist'})
            return resp

    def delete(self, dept_id):
        deleted = del_department(dept_id)
        if deleted:
            resp = jsonify({'message': f'department #{dept_id} deleted'})
            resp.status_code = 200
            return resp
        else:
            resp = jsonify({'message': f'department #{dept_id} does not exist'})
            return resp


dept_api.add_resource(Departments, '/')
dept_api.add_resource(DepartmentItem, '/<int:dept_id>')
