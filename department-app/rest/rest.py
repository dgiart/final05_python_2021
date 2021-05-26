from setup import api, app
from flask_restful import Resource
from flask import request, jsonify
from models.models import Department
from service.database_funcs import add_department, add_employee, add_item


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        data = request.get_json(cache=True)
        print(data)
        # print(request.mimetype)
        return jsonify({'data': data}), 201
    return 'Hop from dep'


class Departments(Resource):
    # def post(self):
    #     data = request.get_json()
    #     title = data.get('title')
    #     # print(type(department))
    #     print(title)
    #     item_id = add_department(title)
    #     # data['id'] = item_id
    #     department = {'title': 'title', 'id': item_id}
    #     # print(department)
    #     resp = jsonify(department)
    #     resp.status_code = 200
    #     return resp

    def get(self):
        p = request.path
        print(p[1:])
        return None

    def post(self):
        data = request.get_json()
        model = request.path[1:]
        item_id = add_item(model=model, **data)
        print(item_id)
        data['id']= item_id
        resp = jsonify(data)
        resp.status_code = 201
        return resp



class Employees(Resource):
    def post(self):
        name = request.json.get('name')
        salary = request.json.get('salary')
        birth = request.json.get('birth')
        print(name)
        item_id = add_employee(name, salary, birth)
        employee = {'id': item_id, 'name': name}
        resp = jsonify(employee)
        resp.status_code = 201
        return resp

    def get(self):
        p = request.path
        print(p)
        return None


api.add_resource(Departments, '/department')
api.add_resource(Employees, '/employee')
