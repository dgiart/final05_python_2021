from dataclasses import dataclass
from collections import Counter


class Departments:
    """ Class departments to store departments,
    name - name of department,
    num - number of employees
    """
    __id = 1
    dept_args = ['id', 'name', 'num']

    def __init__(self, name='None', num=0):
        self.name = name
        self.num = num
        self.id = Departments.__id
        Departments.__id += 1

    def __repr__(self):
        return f'id: {self.id}, name: {self.name}, employees: {self.num}'


@dataclass
class B:
    pass


if __name__ == '__main__':
    l1 = [1, 2, 3]
    d = {1: '', 2: '', 3: ''}
    l2 = d.keys()
    print(Counter(l1) == Counter(l2))
    d = Departments('ss', 2)
    d2 = Departments('ss', 2)
    # for el in dir(Departments):
    #     print(el)
    # print(d2.id)
    # print(Departments.dept_args)
    # for el in dir(d):
    #     print(el)
    # print(B.__qualname__)
    # print(d.__dict__)
    # depts = {}
    # for i in range(1, 10):
    #     d = Departments(f'dep{i}', random.randrange(10, 20))
    #     depts[i] = d
    #     print(depts[i])
    # # for i in range(1, 10):
    # #     print(depts[i])
    #
    # print(depts[5])
