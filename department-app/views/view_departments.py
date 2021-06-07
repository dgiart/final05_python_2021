from flask import Blueprint, render_template, jsonify, request
from service.crud import add_department, get_departments, get_department, del_department, put_department

# from rest.checkers import department_check
view_departments_blueprint = Blueprint('view_departments', __name__, template_folder='templates')


@view_departments_blueprint.route('/', methods=['GET', 'POST'])
def departments_list():
    departments = get_departments()
    return render_template('departments.html', departments=departments)


@view_departments_blueprint.route('/<int:id_dept>', methods=['GET', 'POST'])
def department_item(id_dept):
    department = get_department(id_dept)
    return render_template('department.html', department=department)


