from setup import app
from rest.rest_departments import rest_departments_blueprint
from views.view_departments import view_departments_blueprint
from rest.rest_employees import rest_employees_blueprint
from flask import request, jsonify

app.register_blueprint(rest_departments_blueprint, url_prefix='/rest/departments')
app.register_blueprint(rest_employees_blueprint, url_prefix='/rest/employees')
app.register_blueprint(view_departments_blueprint, url_prefix='/view/departments')



@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        data = request.get_json(cache=True)
        print(data)
        # print(request.mimetype)
        return jsonify({'data': data}), 201
    data = request.get_json(cache=True)
    params = request.args
    if params:
        print('!!!!!!!!!!!!!!!!')
    else:
        print('------------------')
    print(f'data: {data}')
    print(f"GET: {jsonify({'data': data})}")
    return jsonify({'data': data}), 201
    # return 'Hop from dep'


if __name__ == '__main__':
    app.run(debug=True)
