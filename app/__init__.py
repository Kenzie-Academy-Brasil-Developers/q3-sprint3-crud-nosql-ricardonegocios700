from flask import Flask

#from .views import posts as posts_view
from app import views


def create_app():
    app = Flask(__name__, static_folder=None)

    views.init_app(app)

    return app