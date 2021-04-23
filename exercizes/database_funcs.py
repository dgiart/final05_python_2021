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
            cursor.execute(f"CREATE DATABASE {name}")  # .format(name))
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
    # base7 = b.create_base('basefromfunc7', 'art', 'artem', 'localhost')
    # for i in range(2, 8):
    b.drop_base(f'basefromfunc', 'art', 'artem', 'localhost')
    print(b.bases)
