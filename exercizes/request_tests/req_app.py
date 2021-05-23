from flask import Flask, request, jsonify

app = Flask(__name__)


def correct_request(req):
    return req.is_json and 'x' in req.json


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        response = {
            1: 'one',
            2: 'two'
        }
        return jsonify(response), 200
    if request.method == 'POST':
        content_type = request.content_type
        print(request.headers)
        print(content_type)
        # return {0: None}
        data = request.json
        #
        # x = int(data['x'])
        # y = int(data['y'])
        # z = x + y
        # response = {
        #     'z': z
        # }

        return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
