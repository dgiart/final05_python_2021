"""
database_func.py
~~~~~~~~~~~~

This module implements functions which create/drop databases.

"""

import mysql.connector
from mysql.connector import errorcode


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
    # b.create_base('db_to_test', 'art', 'artem', 'localhost')
    # for i in range(2, 8):
    b.drop_base(f'db_to_test', 'art', 'artem', 'localhost')
    print(b.bases)
