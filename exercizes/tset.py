from flask import Flask
from flask_restful import Resource, Api
import requests
import pytest
import sqlalchemy

# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        print('HOP')
        return ' Hi!!!'#{'hello': 'world'}


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    import sys

    # sqlalchemy.create_engine()

    print(sqlalchemy.__version__)
    # print(help(sqlalchemy))

    # sqlalchemy.
    # pytest.
    # url = 'http://iert.kharkov.ua/ru/main.html'
    # res = requests.get(url)
    #
    # txt = res.text
    # with open('iert.txt', 'w', encoding='utf-8') as file:
    #     file.write(txt)

    app.run(debug=True)
