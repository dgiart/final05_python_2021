from flask import Blueprint, render_template
from service.crud import add_employee, get_employees, get_employee, del_employee, put_employee
view_employees_blueprint = Blueprint('view_employees', __name__, template_folder='templates')


@view_employees_blueprint.route('/', methods=['GET', 'POST'])
def employees_list():
    employees = get_employees()
    return render_template('employees.html', employees=employees)


@view_employees_blueprint.route('/<int:id_empl>', methods=['GET', 'POST'])
def employee_item(id_empl):
    employee = get_employee(id_empl)
    return render_template('employee.html', employee=employee)
