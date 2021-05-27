from setup import app
from rest.rest_departments import departments_blueprint
from rest.rest_employees import employees_blueprint
from flask import request, jsonify


app.register_blueprint(departments_blueprint, url_prefix='/departments')
app.register_blueprint(employees_blueprint, url_prefix='/employees')
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        data = request.get_json(cache=True)
        print(data)
        # print(request.mimetype)
        return jsonify({'data': data}), 201
    return 'Hop from dep'

if __name__ == '__main__':
    app.run(debug=True)
