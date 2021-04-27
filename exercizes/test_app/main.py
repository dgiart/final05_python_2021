from app import app
from app import db


@app.route('/')
def index():
    return '<h1>Hello Puppy!</h1>'
if __name__ == '__main__':
    import sys
    print(sys.version)
    app.run(debug = True)
