import pytest
from setup import app
from main import index


@pytest.fixture
def client():
    # app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home(client):

    #test HOME
    rv = client.get("/")
    assert rv.status_code == 200
    assert 'text/html' in rv.content_type

    rv = client.post('/')
    assert rv.status_code == 405
    assert 'text/html' in rv.content_type

    #test REST departments
    rv = client.get("/rest/departments/")
    assert rv.status_code == 200
    assert 'application/json' in rv.content_type

    rv = client.post("/rest/departments/")

    assert rv.status_code == 400
    assert 'application/json' in rv.content_type

    rv = client.post("/rest/departments/", json='aa')

    assert rv.status_code == 400
    assert 'application/json' in rv.content_type

    to_post = {'title': 'test'}
    rv = client.post("/rest/departments/", json=to_post)

    assert rv.status_code == 201
    assert 'application/json' in rv.content_type

    rv = client.get("/rest/departments/1")
    assert rv.status_code == 200
    assert 'application/json' in rv.content_type



    print('*****************************************************************************\n\n')
    print(f'status: {rv.status}')
    print(f'status_code: {rv.status_code}')
    print(f'response: {rv.response}')
    print(f'content_type: {rv.content_type}')
    print(f'data: {rv.data}')

