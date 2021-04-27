import sqlalchemy
import mysql.connector

if __name__ == '__main__':
    engine = sqlalchemy.create_engine('mysql+mysqlconnector://art:artem@localhost/basefromfunc')
    print(engine.dialect)
    print(engine.__doc__)