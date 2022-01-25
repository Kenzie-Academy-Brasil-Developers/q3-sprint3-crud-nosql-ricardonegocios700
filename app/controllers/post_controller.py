from flask import jsonify, request
from http import HTTPStatus

from app.models import Post

def create_post():
    return jsonify({"msg": "create_post ok"}), HTTPStatus.ok