from flask import jsonify, request
from json import dumps
from http import HTTPStatus

from app.models import Post

def new_request():
    return request.get_json()

def seach_post(id):
    post = Post.find_post(int(id))
    post = Post.serialize_id(post)
    return post


def create():
    params = new_request()
    post = Post(**params).save_post()
    post = Post.serialize_id(post)
    return jsonify(post.__dict__), HTTPStatus.CREATED

def delete(id):
    post = seach_post(id)
    try:
        Post.delete_post(post)
    except:
        result = {"type": "error", "msg": "Registro não encontrado", "code": HTTPStatus.NOT_FOUND}
    else:
        result = {"type": "msg", "msg": post, "code": 202}
    return result

def read(id):
    result = seach_post(id)
    if result == None:
        result = {"type": "error", "msg": "Registro não encontrado", "code": HTTPStatus.NOT_FOUND}
    else:
        result = {"type": "msg", "msg": result, "code": HTTPStatus.OK}
    return result

def list():
    result = Post.list_all()
    return {"msg": result}, HTTPStatus.OK

def update(id):
    my_json = new_request()
    post = Post.find_post(int(id))
    if post is None:
        return {'error': "Tentativa de editar post inexistente"}, HTTPStatus.NOT_FOUND
    Post.update_to(int(id), my_json)
    result = seach_post(id)
    return {'msg': result}, HTTPStatus.OK