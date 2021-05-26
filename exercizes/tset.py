from flask import Flask
from flask_restful import Resource, Api
import tempfile
from itertools import count
from collections import Counter
import requests
import pytest
import sqlalchemy

# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        print('HOP')
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')


def foo(model='', **data ):
    print(f'mode; {model}\n')
    print(f'data: {data}')


if __name__ == '__main__':
    print(tempfile.mkstemp())
    import sys
    # d1 = {1: 'one', 2: 'two'}
    # d2 = {2: 'two', 1: 'one'}
    # keys = [2, 1]
    # print(d1 == d2)
    # print(Counter(d1.keys()) == Counter(keys))
    # d = {'a': 'one'}
    # foo(model='MODEL', **d)
    # sqlalchemy.create_engine()

    # print(sqlalchemy.__version__)
    # print(help(sqlalchemy))

    # sqlalchemy.
    # pytest.
    # url = 'http://iert.kharkov.ua/ru/main.html'
    # res = requests.get(url)
    #
    # txt = res.text
    # with open('iert.txt', 'w', encoding='utf-8') as file:
    #     file.write(txt)

    # app.run(debug=True)
