import setup
from datetime import datetime

db = setup.db


# depts_empls=db.Table('depts_empls',
#     db.Column('id_dept', db.Integer, db.ForeignKey('department.id_dept')),
#     db.Column('id_empl', db.Integer, db.ForeignKey('employee.id_empl'))
#
# )


class Department(db.Model):
    id_dept = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(140))
    # employees = db.relationship('Employee', secondary=depts_empls,  backref='department', lazy='dynamic')


    def __init__ (self, *args, **kwargs):
        super(Department, self). __init__(*args, **kwargs)

    def __repr__(self):
        return f'title: {self.title}, id={self.id_dep})'#, employees={self.employees}'


class Employee(db.Model):
    id_empl = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    salary = db.Column(db.Float)
    birthday = db.Column(db.DateTime)
    id_dept = db.Column(db.Integer)#, db.ForeignKey('department.id_dept'))

    def __init__ (self, *args, **kwargs):
        super(Employee, self). __init__(*args, **kwargs)

    def __repr__(self):
        return f'id: {self.id_empl}, name: {self.name}, birthday: {self.birthday}, department: {self.id_dept}'

