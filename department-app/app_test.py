from models.models import Department, Employee
from datetime import datetime
from setup import db
# import random
from flask import Flask, request, render_template
from collections import Counter

# app = Flask(__name__)
# departments = []
# count = 0
#
#
# def correct_request(req_args, model_args):
#     return Counter(req_args) == Counter(model_args)
#
#
# @app.route('/', methods=['POST', 'GET'])
# def index():
#     global count
#     flask_request = request
#     if flask_request.method == 'GET':
#         # dept_args = Departments.dept_args
#         # return {'Departments': dept_args}
#         # return {'departments': departments, 'Departments': dept_args}
#         return render_template('index.html', departments=departments)#, n=name1, m=name2, list=l)
#     if flask_request.method == 'POST':
#         req_args = flask_request.args.to_dict()
#         model_args = Departments.dept_args
#         print(f'flask_request: {flask_request.args}')
#         print(f'req_args = {req_args}')
#         print(f'model_args = {model_args}')
#         print(correct_request(req_args.keys(), model_args))
#         if correct_request(req_args.keys(), model_args):
#             count += 1
#             dep_name = req_args['name']
#             dep_num = req_args['num']
#             # department = Departments(dep_name, dep_num)
#             department = {'id': count, 'name': dep_name, 'num': dep_num}
#             departments.append(department)
#             print(departments)
#             return flask_request.args
#         else:
#             return 'Wrong request'


if __name__ == '__main__':

    e1= Employee(name='TestEmpl')
    # e1.id_empl = 10000
    e1.birthday = datetime.now().date()
    e1.id_dept = 10000
    d1 = Department(title='NewModelTest')
    d1.id_dep = 10000
    d1.employees.append(e1)
    db.session.add(d1)#, d1)
    db.session.commit()
    print(e1)
    # print(d1.employees)


