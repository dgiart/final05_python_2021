"""
crud.py
~~~~~~~~~~~~

This module implements CRUD functions for departments and employees.

"""
from datetime import datetime, date
from setup import db
from models.models import Department, Employee

"""
Departments functions
"""


def add_department(title):
    """
    Adds department to the database db
    :param title: title of department to add
    :return: id of added department
    """
    department = Department(title=title)
    db.session.add(department)
    db.session.commit()
    return department.id_dept


def get_departments():
    """
    Return list of all departments
    :return: list of departments
    """
    departments = Department.query.all()
    to_return = [{'id': department.id_dept, 'title': department.title, 'employees': [
        {'id': employee.id_empl, 'name': employee.name} for employee in department.employees], 'average salary': get_average_salary(department.id_dept)} for department in
                 departments]
    return to_return


def get_department(id_dept):
    """
    Get one department by id.
    :param id_dept: department's id
    :return: department {id: title}
    """
    department = Department.query.filter(Department.id_dept == id_dept).first()
    if department:
        average_salary = get_average_salary(id_dept)
        to_return = {'id': department.id_dept, 'title': department.title, 'average salary': average_salary,
                     'employees': [{'id': employee.id_empl, 'name': employee.name} for employee in
                                   department.employees]}
        return to_return
    else:
        return None


def del_department(dept_id):
    """
    Delete department from db
    :param dept_id:
    :return:
    """
    department = Department.query.filter(Department.id_dept == dept_id).first()
    if department:
        db.session.delete(department)
        db.session.commit()
        return dept_id
    else:
        return None


def put_department(id_dept, title):
    department = Department.query.filter(Department.id_dept == id_dept).first()
    department.title = title
    db.session.commit()
    return id_dept


def get_average_salary(id_dept):
    department = Department.query.filter_by(id_dept=id_dept).first()
    employees = department.employees
    salary = 0
    for employee in employees:
        salary += employee.salary
    return (salary / len(employees)).__round__(2)


"""
Employees functions
"""


def add_employee(name, salary, birthday, id_empl_dept):
    """
    Adds employee to the database db
    :param id_empl_dept: id of department
    :param birthday: birthday of employee
    :param name: name of employee
    :param salary: slary of employee

    :return: employee id
    """
    employee = Employee(name=name, salary=salary, birthday=birthday, id_empl_dept=id_empl_dept)
    db.session.add(employee)
    db.session.commit()
    return employee.id_empl


def get_employees():
    """
    Get all employees
    :return: list of employees dictionaries
    """
    employees = Employee.query.all()
    to_return = [
        {'ID': employee.id_empl, 'Name': employee.name, 'salary': employee.salary, 'birthday': employee.birthday,
         'department': employee.id_empl_dept} for
        employee in employees]
    return to_return


def get_employee(id_empl):
    """
    Get one department by id.
    :param id_empl: department's id
    :return: department {id: title}
    """
    employee = Employee.query.filter(Employee.id_empl == id_empl).first()
    to_return = {'id': employee.id_empl, 'name': employee.name, 'salary': employee.salary,
                 'birthday!!!': employee.birthday, 'department': employee.id_empl_dept}
    return to_return


def del_employee(id_empl):
    """
    Delete department from db
    :param dept_id:
    :return:
    """
    employee = Employee.query.filter(Employee.id_empl == id_empl).first()
    if employee:
        db.session.delete(employee)
        db.session.commit()
        return id_empl
    else:
        return None


def put_employee(id_empl, name, salary, birthday, id_empl_dept):
    employee = Employee.query.filter(Employee.id_empl == id_empl).first()
    employee.name = name
    employee.salary = salary
    employee.birthday = birthday
    employee.id_empl_dept = id_empl_dept
    # db.session.
    db.session.commit()
    return id_empl
