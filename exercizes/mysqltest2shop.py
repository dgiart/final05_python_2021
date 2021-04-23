import mysql.connector
from mysql.connector import errorcode

if __name__ == '__main__':
    DB_NAME = 'epam2021'
    db = mysql.connector.connect(user='art', password='artem',
                                 host='localhost')
    # database=DB_NAME)
    print(db.user)
    print(db.database)
    cursor = db.cursor()
    cursor.execute("use {}".format(DB_NAME))
    cursor.execute("CREATE TABLE departments(did INT NOT NULL AUTO_INCREMENT, "
                   "name varchar(25), number INT, "
                   "PRIMARY KEY(did) )")
    # print(cursor.stored_results())
    # cursor.execute("ALTER TABLE Departments DROP COLUMN Boss_name;")
    # cursor.execute("DELETE FROM usr WHERE usrid=10;")
    # for i in range(10):
    #     cursor.execute("INSERT INTO usr(name) VALUES ('bob');")
    # cursor.execute("SELECT * FROM post where id=5 OR id=6 OR id=7;")
    for el in cursor:
        print(el)
    db.close()
