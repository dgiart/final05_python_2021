from flask import Blueprint, render_template, url_for, redirect
from service.crud import add_employee, get_employees, get_employee, del_employee, put_employee
from datetime import date
from . forms import EmployeeForm
view_employees_blueprint = Blueprint('view_employees', __name__, template_folder='templates')


@view_employees_blueprint.route('/')
def employees_list():
    employees = get_employees()
    return render_template('employees.html', employees=employees)


@view_employees_blueprint.route('/<int:id_empl>')
def employee_item(id_empl):
    employee = get_employee(id_empl)
    return render_template('employee.html', employee=employee)


@view_employees_blueprint.route('/create', methods=['GET', 'POST'])
def create_employee():
    form = EmployeeForm()
    print(f'form name = {form.name.data}')
    print(form.validate_on_submit())
    if form.validate_on_submit():
        print('in')
        name = form.name.data
        salary = form.salary.data
        department = form.department.data
        birthday = date(form.year.data, form.month.data, form.day.data)
        # add_employee(name, salary, birthday, department)
        id_empl = add_employee(name, salary, birthday, department)
        return redirect(url_for('view_employees.employee_item', id_empl=id_empl))
    return render_template('employee_create.html', form=form)


@view_employees_blueprint.route('/delete/<int:id_empl>')
def delete_employee(id_empl):
    deleted = del_employee(id_empl)
    if deleted:
        return redirect(url_for('view_employees.employees_list'))
    else:
        item = 'employee'
        return render_template('not_deleted.html', item=item)



