import sys

# sys.path.append("..")
from setup import app
# import views.view
import rest.rest_api


if __name__ == '__main__':
    app.run(debug=True)
