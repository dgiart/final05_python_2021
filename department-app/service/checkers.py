from collections import Counter
from datetime import datetime
from models.models import Department, Employee


def has_value(data: dict, model_keys: list) -> bool:
    for key in model_keys:
        try:
            if not data.get(key):
                return False
        except AttributeError as e:
            print(f'AttributeError in check {e}')
            return False
    return True


def get_date(date):
    try:
        date = datetime(date.get('year'), date.get('month'), date.get('day'))
        return date.date()
    except ValueError as e:
        return False


def department_check(data: dict, model_keys: list) -> bool:
    if not has_value(data, model_keys) or not (Counter(data.keys()) == Counter(model_keys)) or not isinstance(
            data['title'], str):

        return False

    return True

def is_in_department(id_empl_dept):
    return Department.query.filter_by(id_dept=id_empl_dept).first()


def employee_check(data: dict, model_keys: list) -> bool:
    print(f'model_keys = {model_keys}')
    if not has_value(data, model_keys) or not (Counter(data.keys()) == Counter(model_keys)) \
            or not isinstance(data['name'], str) \
            or not isinstance(data['salary'], float) \
            or not isinstance(data['birthday'], dict) \
            or not is_in_department(data.get('id_empl_dept')):
            # or not Department.query.filter(id_dept=data.get('id_empl_dept')).first():

        print(f'employee_check returns False')
        return False
    else:
        print(f'employee_check returns birthday')
        return get_date(data['birthday'])
