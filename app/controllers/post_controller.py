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
    except TypeError:
        result = {"msg": "Registro não encontrado", "code": HTTPStatus.NOT_FOUND}
    else:
        result = {"msg": post, "code": 202}
    return result

def read(id):
    result = seach_post(id)
    if result == None:
        result = {"msg": "Registro não encontrado", "code": HTTPStatus.NOT_FOUND}
    else:
        result = {"msg": result, "code": HTTPStatus.OK}
    return result

def list():
    result = Post.list_all()
    return {"msg": result}, HTTPStatus.OK

def update(id):
    params = new_request()
    post = Post.find_post(int(id))
    new = Post(**post)
    print("000000000000000000000000000000",params['title'])
    print("111111111111111111111111111111",type(params))
    print("222222222222222222222222222222",type(post))
    print("33333333333333333333333333333333",type(new))
    print("44444444444444444444444444444444",new)
    result = new.update_to(params)
    return {"msg": "result"}