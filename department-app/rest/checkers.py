from collections import Counter

department_keys = ['title']


def department_check(data):
    if not data or not (Counter(data.keys()) == Counter(department_keys)) or not isinstance(data['title'], str):
        return False
    return True
