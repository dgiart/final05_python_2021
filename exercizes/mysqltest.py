from sqlalchemy import create_engine
import mysql.connector

if __name__ == '__main__':
    # db = create_engine('mysql://root:qt217gb314@localhost/test1')
    DB_NAME = 'epm2021'
    db = mysql.connector.connect(user='art', password='artem',
                                 host='localhost',
                                 database=DB_NAME)
    # db = mysql.connector.connect(user='art', password='artem', host='localhost', database)
    print(db.user)
    print(db.database)
    cursor = db.cursor()
    # print(f'cursor: {cursor}')
    # for el in dir(cursor):
    #     print(el)
    # cursor.execute("USE {}".format(DB_NAME))
    # cursor.execute("SHOW TABLES")
    # cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    # cursor.execute(f"DROP DATABASE {DB_NAME}")
    # cursor.execute("ALTER TABLE Departments ADD COLUMN Boss_name varchar(255);")
    departments = {}
    cursor.execute("SELECT * FROM Departments;")
    deps_number = 0
    for el in cursor:
        departments[el[0]] = {'num': el[1], 'name': el[2], 'boss': el[3]}
        deps_number += 1
        # addboss.execute(f"INSERT INTO table_name (NumberEmpls, Name, Boss_name) VALUES ({el[1]}, {el[2]}, {'boss'});")
        # print(el)
    departments[2]['boss'] = 'Art'
    departments[3]['boss'] = 'Bob'
    names = ['Art', 'Bob']

    print(departments)
    addboss = db.cursor()
    # addboss.execute("SELECT * FROM Departments;")
    for i in range(2, deps_number + 2):
        addboss.execute(f"INSERT INTO Departments (NumberEmpls, Name, Boss_name) VALUES ('{departments[i]['num']}', '{departments[i]['name']}', 'boss');")
    # print(type(cursor))
    db.close()
    print('DONE')
