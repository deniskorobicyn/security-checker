from flask import Blueprint, request
vulnerabilities = Blueprint('vulnerabilities', __name__)

@vulnerabilities.route("/", methods=['GET'])
def index():
    return "ok"
