# Third party modules
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    db.init_app(app)

    @app.route("/square")
    def square():
        number = int(request.args.get("number", 0))
        return str(number ** 2)

    return app


if __name__ == "__main__":
    app = create_app()
    print(db)
    app.run()