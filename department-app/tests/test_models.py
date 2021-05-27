from models.models import Department, Employee
import pytest


@pytest.fixture
def employee_to_test():
    name = 'Jon'
    salary = 5000
    birth = 1979
    employee = Employee(name=name, salary=salary, birth=birth)
    yield employee


def test_department():
    d = Department(title='xxxx')
    assert d.title == 'xxxx'


def test_employee_name(employee_to_test):
    assert employee_to_test.name == 'Jon'


def test_employee_salary(employee_to_test):
    assert employee_to_test.salary == 5000


def test_employee_birth(employee_to_test):
    assert employee_to_test.birth == 1979
