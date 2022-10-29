
from .users.views import users
from flask import Blueprint

api_v1 = Blueprint('v1', __name__, url_prefix='/v1')

api_v1.register_blueprint(users)