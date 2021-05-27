from setup import app
from rest.rest_departments import departments_blueprint
from rest.rest_employees import employees_blueprint


app.register_blueprint(departments_blueprint, url_prefix='/departments')
app.register_blueprint(employees_blueprint, url_prefix='/employees')

if __name__ == '__main__':
    app.run(debug=True)
