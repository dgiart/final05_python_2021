from sqlalchemy import  create_engine
import mysql.connector


if __name__ == '__main__':
    # db = create_engine('mysql://root:qt217gb314@localhost/test1')
    DB_NAME = 'epm2021'
    # db = mysql.connector.connect(user='root', password='qt217gb314',
    #                               host='localhost',
    #                               database='test1')
    db = mysql.connector.connect(user='root', password='root')
    print(db.user)
    print(db.database)
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    cursor.execute(f"DROP DATABASE {DB_NAME}")

    # db.
    db.close()