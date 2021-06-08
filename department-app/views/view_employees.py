from flask import Blueprint, render_template, url_for, redirect
from service.crud import add_employee, get_employees, get_employee, del_employee, put_employee
from datetime import date
from . forms import EmployeeForm, BirthDateForm, DateTest
from service.checkers import is_in_department
view_employees_blueprint = Blueprint('view_employees', __name__, template_folder='templates')

@view_employees_blueprint.route('/test', methods=['GET', 'POST'])
def datetime():
    form = DateTest()
    if form.validate_on_submit():
        print('!!')
        print(form.date.data.year)

    return render_template('date_test.html', form=form)



@view_employees_blueprint.route('/', methods=['GET', 'POST'])
def employees_list():
    employees = get_employees()
    form = BirthDateForm()
    if form.validate_on_submit():
        dates = form.start_date.data.year, form.start_date.data.month, form.start_date.data.day, form.end_date.data.year, form.end_date.data.month, form.end_date.data.day
        employees = get_employees(dates)
        return render_template('employees.html', employees=employees, form=form)
    return render_template('employees.html', employees=employees, form=form)


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
        print(department)
        if not is_in_department(department):
            item = 'department'
            return render_template('not_existed.html', item=item)
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
        return render_template('not_existed.html', item=item)



