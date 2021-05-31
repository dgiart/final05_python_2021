"""
crud.py
~~~~~~~~~~~~

This module implements CRUD functions for departments and employees.

"""
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
    to_return = [{d.id_dept: d.title} for d in departments]
    return to_return


def get_department(dept_id):
    """
    Get one department by id.
    :param dept_id: department's id
    :return: department {id: title}
    """
    department = Department.query.filter(Department.id_dept == dept_id).first()
    if department:
        to_return = {department.id_dept: department.title}
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


"""
Employees functions
"""


def add_employee(name, salary, birth):
    """
    Adds employee to the database db
    :param name: name of employee
    :param salary: slary of employee
    :param birth: birth year employee
    :return: employee id
    """
    employee = Employee(name=name, salary=salary, birth=birth)
    db.session.add(employee)
    db.session.commit()
    return employee.id_empl


def get_employees():
    """
    Get all employees
    :param id_empl: employee's id
    :return: list of emloyees dictionaris
    """
    emloyees = Employee.query.all()
    to_return = [{'ID': employee.id_empl, 'Name': employee.name, 'salary': employee.salary, 'birth': employee.birthday} for
                 employee in emloyees]
    return to_return


def get_employee(id_empl):
    """
    Get one department by id.
    :param dept_id: department's id
    :return: department {id: title}
    """
    employee = Employee.query.filter(Employee.id_empl == id_empl).first()
    to_return = {'id': employee.id_empl, 'name': employee.name, 'salary': employee.salary, 'birth': employee.birth}
    return to_return
