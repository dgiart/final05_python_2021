from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand

# from flask_admin import Admin
# from flask_admin.contrib.sqla import ModelView
#
# from flask_security import SQLAlchemyUserDatastore
# from flask_security import Security


app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)
Migrate(app,db)
