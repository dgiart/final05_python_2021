import sys
sys.path.insert(0, '.')
from app import db

department_keys = ['title']
employee_keys = ['name', 'salary', 'birthday', 'id_empl_dept']


class Department(db.Model):
    id_dept = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(140))
    employees = db.relationship('Employee', backref='employee_department')


    def __init__ (self, *args, **kwargs):
        super(Department, self). __init__(*args, **kwargs)

    def __repr__(self):
        return f'Department: id={self.id_dept}, title: {self.title})'#, employees={self.employees}'


class Employee(db.Model):
    id_empl = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(140))
    salary = db.Column(db.Float)
    birthday = db.Column(db.DateTime)
    id_empl_dept = db.Column(db.Integer, db.ForeignKey('department.id_dept'))

    def __init__ (self, *args, **kwargs):
        super(Employee, self). __init__(*args, **kwargs)


