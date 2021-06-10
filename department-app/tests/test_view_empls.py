import pytest
import sys
sys.path.insert(0, '.')
from service.app_to_test.app import test_app
from main import index


@pytest.fixture
def client():
    test_app.config["TESTING"] = True
    with test_app.test_client() as client:
        yield client


def test_rest(client):
    # test VIEW employees
    rv = client.get('/view/employees/')
    assert rv.status_code == 200
    assert 'text/html' in rv.content_type
    assert 'Enter birthday interval to search' in str(rv.data)

    rv = client.post('/view/employees/')
    assert rv.status_code == 200
    assert 'text/html' in rv.content_type

    rv = client.get('/view/employees/1')
    assert rv.status_code == 200
    assert 'text/html' in rv.content_type
    assert 'Birthday:' in str(rv.data)

    rv = client.post('/view/employees/2')
    assert rv.status_code == 405
    assert 'text/html' in rv.content_type

    rv = client.get('/view/employees/create')
    assert rv.status_code == 200
    assert 'text/html' in rv.content_type
    assert 'Add new Employee' in str(rv.data)

    rv = client.post('/view/employees/create')
    assert rv.status_code == 200
    assert 'text/html' in rv.content_type
    assert 'Add new Employee' in str(rv.data)

    rv = client.put('/view/employees/create')
    assert rv.status_code == 405
    assert 'text/html' in rv.content_type

    rv = client.get('/view/employees/edit/2')
    assert rv.status_code == 200
    assert 'text/html' in rv.content_type
    assert 'Edit Employee #' in str(rv.data)

    rv = client.post('/view/employees/edit/2')
    assert rv.status_code == 200
    assert 'text/html' in rv.content_type
    assert 'Edit Employee #' in str(rv.data)

    rv = client.get('/view/employees/delete/202')
    assert rv.status_code == 200
    assert 'text/html' in rv.content_type
    assert 'does not exist' in str(rv.data)

    rv = client.get('/view/employees/delete/11')
    assert rv.status_code == 302
    assert 'text/html' in rv.content_type
    assert 'You should be redirected' in str(rv.data)
    # Department  #



    print('*****************************************************************************\n\n')
    print(f'status: {rv.status}')
    print(f'status_code: {rv.status_code}')
    print(f'response: {rv.response}')
    print(f'content_type: {rv.content_type}')
    print(f'data: {rv.data}')
