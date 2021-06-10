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
    # test VIEW departments
    rv = client.get('/view/departments/')
    assert rv.status_code == 200
    assert 'text/html' in rv.content_type
    assert 'List of Departments' in str(rv.data)

    rv = client.put('/view/departments/')
    assert rv.status_code == 405
    assert 'text/html' in rv.content_type

    to_put = {'title': 'test'}
    rv = client.post('/view/departments/', json=to_put)
    assert rv.status_code == 405
    assert 'text/html' in rv.content_type

    rv = client.get('/view/departments/32')
    assert rv.status_code == 200
    assert 'text/html' in rv.content_type
    assert 'Number of Employees' in str(rv.data)

    rv = client.post('/view/departments/22')
    assert rv.status_code == 405
    assert 'text/html' in rv.content_type

    rv = client.get('/view/departments/create')
    assert rv.status_code == 200
    assert 'text/html' in rv.content_type
    assert 'Create new Department' in str(rv.data)

    to_put = {'title': 'test'}
    rv = client.post('/view/departments/create', json=to_put)
    assert rv.status_code == 200
    assert 'text/html' in rv.content_type
    assert 'Create new Department' in str(rv.data)

    rv = client.get('/view/departments/delete/202')
    assert rv.status_code == 200
    assert 'text/html' in rv.content_type
    assert 'does not exist' in str(rv.data)

    rv = client.get('/view/departments/delete/44')
    assert rv.status_code == 302
    assert 'text/html' in rv.content_type
    assert 'You should be redirected' in str(rv.data)

    rv = client.get('/view/departments/edit/1')
    assert rv.status_code == 200
    assert 'text/html' in rv.content_type
    assert 'Enter a Title' in str(rv.data)

    rv = client.post('/view/departments/edit/1')
    assert rv.status_code == 200
    assert 'text/html' in rv.content_type
    assert 'Enter a Title' in str(rv.data)

    tu_put = {'title': 'research'}
    rv = client.post('/view/departments/edit/1', json=tu_put)
    assert rv.status_code == 200
    assert 'text/html' in rv.content_type
    assert 'Enter a Title' in str(rv.data)












    print('*****************************************************************************\n\n')
    print(f'status: {rv.status}')
    print(f'status_code: {rv.status_code}')
    print(f'response: {rv.response}')
    print(f'content_type: {rv.content_type}')
    print(f'data: {rv.data}')
