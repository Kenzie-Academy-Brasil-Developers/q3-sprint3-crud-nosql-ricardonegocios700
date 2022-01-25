from flask import jsonify, request
from json import dumps
from http import HTTPStatus

from app.models import Post

def new_request():
    return request.get_json()

def create():
    params = new_request()
    post = Post(**params).save_post()
    #breakpoint()
    post = Post.serialize_id(post)
    return jsonify(post.__dict__), HTTPStatus.OK

def delete(id):
    post = Post.find_post(int(id))
    post = Post.serialize_id(post)
    try:
        Post.delete_post(post)
    except TypeError:
        return {"msg": "Registro não encontrado"}
    return jsonify(post)