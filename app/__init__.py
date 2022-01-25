from flask import Flask

#from .views import posts as posts_view
from app import views

app = Flask(__name__)#, static_folder=None)

# @app.get("/")
# def home():
#     return "Bom dia"
def create_app():

    views.init_app(app)
    
    return app