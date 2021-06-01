from collections import Counter
from datetime import datetime


# department_keys = ['title']

def has_value(data: dict, model_keys: list) -> bool:
    for key in model_keys:
        if not data.get(key):
            print('NOT')
            return False
    return True


def get_date(date):
    try:
        date = datetime(date.get('year'), date.get('month'), date.get('day'))
        return date.date()
    except ValueError as e:
        print(e)
        return False


def department_check(data: dict, model_keys: list) -> bool:
    # print(f"type(data['title']): {type(data['title'])}")
    if not has_value(data, model_keys) or not (Counter(data.keys()) == Counter(model_keys)) or not isinstance(
            data['title'], str):
        return False
    return True


def employee_check(data: dict, model_keys: list) -> bool:
    if not has_value(data, model_keys) or not (Counter(data.keys()) == Counter(model_keys)) \
            or not isinstance(data['name'], str) \
            or not isinstance(data['salary'], float) \
            or not isinstance(data['birthday'], dict):
        print('here: {},')
        return False
    else:
        return get_date(data['birthday'])
