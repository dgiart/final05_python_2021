from models.models import Department, Employee
import random
from datetime import datetime
from setup import db
from datetime import date
# from numpy import np
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
def add_dept_to_empl():
    depts = [1]#, 2, 4, 5, 43]
    # print(datetime.now().date())
    employees = Employee.query.all()
    for empl in employees:
        # i = random.randint(0, 4)
        empl.id_empl_dept = depts[0]


def add_birth_to_empl():
    employees = Employee.query.all()
    for empl in employees:
        year = random.randint(1970, 2001)
        month = random.randint(1, 12)
        day = random.randint(1, 30)

        print(date(year, month, day))
        empl.birthday = date(year, month, day)


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def get_average_salary(id_dept):
    department = Department.query.filter_by(id_dept=id_dept).first()
    employees = department.employees
    salary = 0
    for employee in employees:
        salary += employee.salary
    return (salary / len(employees)).__round__(2)


if __name__ == '__main__':
    add_dept_to_empl()
    # print(get_average_salary(1))
    # employees = Employee.query.all()
    # def foo(a):
    #     print(a)
    # l = [1, 2, 3]
    # m = map(print, l)
    # tuple(m)
    # print('\n ************************************************************************************************\n')
    # print(f'm = {list(m)}')
    # print(f'l = {l}')
    # ees = list(map(lambda employee: employee.birthday.year >= 1983, [employee for employee in employees ]))#if employee.birthday.year >= 1983]))
    # ees = [employee for employee in employees if datetime(1983, 8, 5) <= employee.birthday <= datetime(1983, 8, 5)]
    # print(ees)
    # for employee in employees:
    #     if employee.birthday.year == 1983:
    #         print(employee)
    # for el in dir(Employee.birthday):
    #     print(el)
    # add_birth_to_empl()
    # add_dept_to_empl()
    # print(e2.birthday.year)
    # e1.id_empl = 10000
    # e2.birthday = datetime.now().date()
    # e2.id_empl_dept = 1
    d1 = Department.query.filter_by(id_dept=1).first()
    # d1.title = 'study'
    # db.session.add(e2)
    # db.session.add(d1)
    # db.session.commit()
    # print(d1.employees)
    for empl in d1.employees:
        print(f'{empl.name}, {empl.salary}, {empl.birthday.year}')
    print(d1.employees)
