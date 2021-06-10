from models.models import Department, Employee
from datetime import date
import pytest
from setup import db


@pytest.fixture
def employee_to_test():
    name = 'Juuuuk'
    salary = 5000
    birthday = date(1979, 3, 15)
    employee = Employee(name=name, salary=salary, birthday=birthday)
    yield employee


@pytest.fixture
def id_to_test():
    name = 'Jk'
    salary = 5000
    birthday = date(1979, 3, 15)
    employee = Employee(name=name, salary=salary, birthday=birthday)
    db.session.add(employee)
    db.session.commit()
    yield employee.id_empl


def test_department():
    d = Department(title='xxxx')
    assert d.title == 'xxxx'


def test_employee_name(employee_to_test):
    assert employee_to_test.name == 'Jon'


def test_employee_salary(employee_to_test):
    assert employee_to_test.salary == 5000


def test_employee_birth(employee_to_test):
    assert employee_to_test.birthday.year == 1979


def test_employee_query(employee_to_test):
    q = Department.query.all()
    assert len(q) == 1


def test_db(employee_to_test):
    db.session.add(employee_to_test)
    db.session.commit()
    q = Employee.query.filter_by(id_empl=employee_to_test.id_empl).first()
    assert q.id_empl == employee_to_test.id_empl


def test_id(id_to_test):
    assert id_to_test == 1
