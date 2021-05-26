from models.models import Department
from setup import db

def test_dept():
    d = Department(title='xxxx')
    db.session.add(d)
    db.session.commit()
    # assert d.title == 'yyy'
    assert d.id_dept == 3