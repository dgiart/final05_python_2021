from app import db, test_app
from datetime import date
from models_totest import Department, Employee
import sys
sys.path.insert(0, '../..')
from main import index


test_app.config["TESTING"] = True
db.create_all()
client = test_app.test_client()
for i in range(50):
    bd = date(1950 + i, 11, 20)
    e = Employee(name=f'tName{i}', salary=1000*i/50, birthday=bd, id_empl_dept=i)
    db.session.add(e)
    db.session.commit()

for i in range(50):
    d = Department(title=f'test title {i}')
    db.session.add(d)
    db.session.commit()
# bd = date(1980, 11, 20)
# e = Employee(name='tName', salary=1000, birthday=bd, id_empl_dept=1)
# db.session.add(m)
# db.session.add(e)
# db.session.commit()
deps = Department.query.all()
empls = Employee.query.all()
print(len(deps))
print('***********************')
for empl in empls:
    print(empl)
for dept in deps:
    print(dept)
# to_post = {'title': 'test'}
# rv = client.post("/rest/departments/", json=to_post)
# print(rv.data)