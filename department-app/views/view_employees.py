from flask import Blueprint, render_template, url_for, redirect
from service.crud import add_employee, get_employees, get_employee, del_employee, put_employee
from datetime import date
from . forms import EmployeeForm, BirthDateIntervalForm, BirthDateForm
from service.checkers import is_in_department
view_employees_blueprint = Blueprint('view_employees', __name__, template_folder='templates')

# @view_employees_blueprint.route('/test', methods=['GET', 'POST'])
# def datetime():
#     form = DateTest()
#     if form.validate_on_submit():
#         print('!!')
#         print(form.date.data.year)
#
#     return render_template('date_test.html', form=form)



@view_employees_blueprint.route('/', methods=['GET', 'POST'])
def employees_list():
    employees = get_employees()
    form1 = BirthDateForm()
    form2 = BirthDateIntervalForm()
    print(f'form1.validate_on_submit(): {form1.validate_on_submit()}')
    print(f'form1.birthday.data: {form1.birthday.data}')
    print(f'form2.validate_on_submit(): {form2.validate_on_submit()}')
    print(f'form2.start_date.data: {form2.start_date.data}')
    print(f'form2.end_date.data: {form2.end_date.data}')

    if form1.validate_on_submit() and form1.birthday.data:
        print('!!')
        print(form1.is_submitted())
        dates = form1.birthday.data.year, form1.birthday.data.month, form1.birthday.data.day, form1.birthday.data.year, form1.birthday.data.month, form1.birthday.data.day
        employees = get_employees(dates)
        temp_form = form1
        return render_template('employees.html', employees=employees, form1=temp_form, form2=form2)

    if form2.validate_on_submit() and form2.start_date.data and form2.end_date.data:
        dates = form2.start_date.data.year, form2.start_date.data.month, form2.start_date.data.day, form2.end_date.data.year, form2.end_date.data.month, form2.end_date.data.day
        employees = get_employees(dates)
        return render_template('employees.html', employees=employees, form1=form1, form2=form2)
    return render_template('employees.html', employees=employees, form1=form1, form2=form2)


@view_employees_blueprint.route('/<int:id_empl>')
def employee_item(id_empl):
    print('!!')
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



