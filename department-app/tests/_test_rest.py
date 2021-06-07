from rest.rest_api import index


def test_index():
    assert index() == 'Hello'
