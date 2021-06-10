from flask import Flask

app = Flask(__name__)

@app.route('/')
def hi():
    to_return = ['a', 'b']
    return 'to_return'

if __name__ == '__main__':
    app.run(port = 8000, debug = True)
