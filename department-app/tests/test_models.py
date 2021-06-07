from models.models import Department, Employee
from datetime import date
import pytest


@pytest.fixture
def employee_to_test():
    name = 'Jon'
    salary = 5000
    birthday = date(1979, 3, 15)
    employee = Employee(name=name, salary=salary, birthday=birthday)
    yield employee


def test_department():
    d = Department(title='xxxx')
    assert d.title == 'xxxx'


def test_employee_name(employee_to_test):
    assert employee_to_test.name == 'Jon'


def test_employee_salary(employee_to_test):
    assert employee_to_test.salary == 5000


def test_employee_birth(employee_to_test):
    assert employee_to_test.birthday.year == 1979
