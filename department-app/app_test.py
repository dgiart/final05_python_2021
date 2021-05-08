from models.models import Departments
import random
from flask import Flask, request
from collections import Counter

app = Flask(__name__)
departments = []


def correct_request(req_args, model_args):
    return Counter(req_args) == Counter(model_args)


@app.route('/', methods=['POST', 'GET'])
def index():
    flask_request = request
    if flask_request.method == 'GET':
        return {'departments': departments, 'Departments': Departments.dept_args}
    if flask_request.method == 'POST':
        req_args = flask_request.args.to_dict()
        model_args = Departments.dept_args
        print(f'req_args = {req_args}')
        print(f'model_args = {model_args}')
        print(correct_request(req_args.keys(), model_args))
        if correct_request(req_args.keys(), model_args):
            dep_name = req_args['name']
            dep_num = req_args['num']
            department = Departments(dep_name, dep_num)
            departments.append(department)
            print(departments)
            return flask_request.args
        else:
            return 'Wrong request'


if __name__ == '__main__':
    app.run(debug=True)
