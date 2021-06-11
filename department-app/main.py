from setup import app, db
from rest.rest_departments import rest_departments_blueprint
from views.view_departments import view_departments_blueprint
from views.view_employees import view_employees_blueprint
from rest.rest_employees import rest_employees_blueprint
from flask import render_template, request, jsonify
from models.models import Department, Employee
db.create_all()

app.register_blueprint(rest_departments_blueprint, url_prefix='/rest/departments')
app.register_blueprint(rest_employees_blueprint, url_prefix='/rest/employees')
app.register_blueprint(view_departments_blueprint, url_prefix='/view/departments')
app.register_blueprint(view_employees_blueprint, url_prefix='/view/employees')


@app.route('/')
def index():
    data = request.get_json()
    print(data)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
