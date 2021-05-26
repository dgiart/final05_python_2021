# """
# database_func.py
# ~~~~~~~~~~~~
#
# This module implements functions which manipulate databases.
#
# """
#
#
#
import mysql.connector
# from setup import db
# from mysql.connector import errorcode
# from models.models import Department, Employee
#
# models_dict = {
#     'department': Department,
#     'employee': Employee
# }
# id_dict = {
#     'Department': 'id_dept',
#     'Employee': 'id_empl'
# }
#
#
# def add_item(model='', **data):
#     model_class = models_dict[model]
#     for el in dir(model_class):
#         print(el)
#     # if model == 'department':
#     #     title = data['title']
#     #     department = Department(title=title)
#     #     db.session.add(department)
#     #     db.session.commit()
#     #     return department.id_dept
#     # else:
#     #     pass
#
#
# def add_department(title):
#     """
#     Adds department to the database db
#     :param title: title of department to add
#     :return: id of added department
#     """
#     department = Department(title=title)
#     db.session.add(department)
#     db.session.commit()
#     return department.id_dept
#
#
# def get_departments():
#     departments = Department.query.all()
#     to_return = [{d.id_dept: d.title} for d in departments]
#     return to_return
#
# def get_department(dept_id):
#     department = Department.query.filter(Department.id_dept == dept_id).first()
#     to_return = {department.id_dept: department.title}
#     return to_return
#
#
# def add_employee(name, salary, birth):
#     employee = Employee(name=name, salary=salary, birth=birth)
#     db.session.add(employee)
#     db.session.commit()
#     return employee.id_empl


class Database:
    def __init__(self):
        self.bases = {}

    # @staticmethod
    def create_base(self, name, user, password, host):
        try:
            db = mysql.connector.connect(user=user, password=password,
                                         host=host)
            cursor = db.cursor()
            cursor.execute(f"CREATE DATABASE {name} CHARACTER SET UTF8 COLLATE UTF8_UNICODE_CI")  # .format(name))

            self.bases[name] = db
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)
        finally:
            try:
                db.close()
            finally:
                return self.bases

    def drop_base(self, name, user, password, host):
        try:
            db = mysql.connector.connect(user=user, password=password,
                                         host=host)
            cursor = db.cursor()
            cursor.execute(f"DROP DATABASE {name}")  # .format(name))
            # self.bases[name].__delitem__(name)
        finally:
            db.close()


if __name__ == '__main__':
    b = Database()
    b.create_base('departments', 'art', 'artem', 'localhost')
    # for i in range(2, 8):
    # b.drop_base(f'departments', 'art', 'artem', 'localhost')
    print(b.bases)