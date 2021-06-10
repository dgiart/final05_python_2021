from app import db
from models import Department
from department_app.main import index

# db.create_all()
# m = Department(title='testtaitle')
# db.session.add(m)
# db.session.commit()
# print(m.id_dept)

import sys
for el in sys.path:
    print(el)