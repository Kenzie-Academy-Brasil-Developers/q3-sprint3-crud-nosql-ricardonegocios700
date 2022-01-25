from .posts import post_route

def init_app(app):
    post_route(app)