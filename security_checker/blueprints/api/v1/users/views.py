from flask import Blueprint, request
users = Blueprint('users', __name__)

@users.route("/", methods=['POST'])
def login():
    return "ok"
