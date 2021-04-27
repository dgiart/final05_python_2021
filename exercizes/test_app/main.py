from app import app
from app import db



if __name__ == '__main__':
    import sys
    print(sys.version)
    app.run(debug = True)
