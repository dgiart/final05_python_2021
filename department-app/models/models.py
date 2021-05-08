import random


class Departments:
    __id = 0
    dept_args = ['id', 'name', 'num']

    def __init__(self, name='None', num=0):
        self.name = name
        self.num = num
        Departments.__id += 1
        self.id = Departments.__id

    def __repr__(self):
        return f'id: {self.id}; name: {self.name}; employees: {self.num}'
