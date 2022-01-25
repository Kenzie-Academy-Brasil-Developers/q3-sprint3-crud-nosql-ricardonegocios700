from app.controllers.post_controller import create_post

def post_route(app):
    @app.post("/post")
    def post_in():
        return "create_post()"