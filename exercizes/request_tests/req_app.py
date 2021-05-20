from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        response = {
            1: 'one',
            2: 'two'
        }
        return jsonify(response), 404


if __name__ == '__main__':
    app.run(debug=True)
