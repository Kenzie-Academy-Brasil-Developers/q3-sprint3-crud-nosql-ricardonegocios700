from flask import jsonify
from app.controllers.post_controller import create, delete

def post_route(app):
    @app.post("/posts")
    # não preciso passar o app a partir daqui, 
    # o request não necessita dele
    def create_post():
        return create()
        
    @app.delete("/posts/<id>")
    def delete_post(id):
        return delete(int(id))