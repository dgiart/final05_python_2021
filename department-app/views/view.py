from setup import app, api, db
from flask_restful import Resource
from flask import request, jsonify
from models.models import Department


@app.route('/')
def index():
    return 'Hop from dep'


class Departments(Resource):
    def post(self):
        title = request.json.get('title')
        print(title)
        department = Department(title=title)
        db.session.add(department)
        db.session.commit()
        return jsonify({'department': title})


api.add_resource(Departments, '/departments')
