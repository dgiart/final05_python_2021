import mysql.connector
from setup import db
from mysql.connector import errorcode
from models.models import Department, Employee


def add_department(title):
    department = Department(title=title)
    db.session.add(department)
    db.session.commit()


def add_employee(name, salary, birth):
    employee = Employee(name=name, salary=salary, birth=birth)
    db.session.add(employee)
    db.session.commit()


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
