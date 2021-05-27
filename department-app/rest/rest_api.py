from setup import api, app
from flask_restful import Resource
from flask import request, jsonify
from service.database_funcs import add_department, add_employee, get_departments, get_department
from rest.checkers import department_check


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        data = request.get_json(cache=True)
        print(data)
        # print(request.mimetype)
        return jsonify({'data': data}), 201
    return 'Hop from dep'


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
        p = request.path
        print(p)
        return None


class DepartmentItem(Resource):
    def get(self, dept_id):
        department = get_department(dept_id)
        print(f"get department: {dept_id}")
        resp = jsonify(department)
        resp.status_code = 200
        return resp


# api.add_resource(Departments, '/departments')
# api.add_resource(DepartmentItem, '/departments/<int:dept_id>')
# api.add_resource(Employees, '/employees')
