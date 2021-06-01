from flask import Blueprint, jsonify, request
from flask_restful import Resource, Api
from service.crud import add_department, get_departments, get_department, del_department, put_department
from rest.checkers import department_check
from models.models import department_keys
rest_departments_blueprint = Blueprint('departments', __name__)
dept_api = Api(rest_departments_blueprint)


class Departments(Resource):
    def post(self):
        """
        Create department with data from POST reuest body.json
        :return: departmen id, title
        """
        data = request.get_json()
        if not department_check(data, department_keys):
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
    def get(self, id_dept):
        """
        Method get department id from url and gets corresponding department
        :param dept_id: department id
        :return: if success -> department info, if not -> message': department with id does not exist
        """
        department = get_department(id_dept)
        if department:
            print(f"get department: {id_dept}")
            resp = jsonify(department)
            resp.status_code = 200
            return resp
        else:
            resp = jsonify({'message': f'department #{id_dept} does not exist'})
            return resp

    def delete(self, id_dept):
        """
        Method get department id from url and deletes corresponding department
        :param dept_id: department id
        :return: if success -> department id, if not -> message': department with id does not exist
        """
        deleted = del_department(id_dept)
        if deleted:
            resp = jsonify({'message': f'department #{id_dept} deleted'})
            resp.status_code = 200
            return resp
        else:
            resp = jsonify({'message': f'department #{id_dept} does not exist'})
            return resp

    def put(self, id_dept):
        data = request.get_json()
        if not department_check(data, department_keys):
            return 'Bad Request', 400
        title = data.get('title')
        item_id = put_department(id_dept, title)
        employee = {'id': item_id, 'title': title}
        resp = jsonify(employee)
        resp.status_code = 201
        # resp = None
        return resp


dept_api.add_resource(Departments, '/')
dept_api.add_resource(DepartmentItem, '/<int:id_dept>')
