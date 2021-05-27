import setup
from datetime import datetime

db = setup.db


class Department(db.Model):
    id_dept = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(140))
    empoyees = db.relationship('Employee', backref='department',
                    lazy='dynamic')

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return f'name: {self.title}, id={self.id_dep}'


class Employee(db.Model):
    id_empl = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    salary = db.Column(db.Float)
    birth = db.Column(db.DateTime)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id_dept'))
