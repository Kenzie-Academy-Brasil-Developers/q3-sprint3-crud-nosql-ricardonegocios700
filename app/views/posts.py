from flask import jsonify
from app.controllers.post_controller import create, delete, read, list, update

def post_route(app):
    @app.post("/posts")
    # não preciso passar o app a partir daqui, 
    # o request não necessita dele
    def create_post():
        return create()
        
    @app.delete("/posts/<id>")
    def delete_post(id):
        result = delete(int(id))
        # return jsonify(result["msg"]), result["code"]
        return {"msg": result["msg"]}, result["code"]

    @app.get("/posts/<id>")
    def read_post_by_id(id):
        result = read(id)
        return {"msg": result["msg"]}, result["code"]

    @app.get("/posts")
    def read_posts():
        return list()

    @app.patch("/posts/<id>")
    def update_post(id):
        # return {"msg": f"update {id}"}
        return update(id)