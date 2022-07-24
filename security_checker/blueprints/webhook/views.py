from flask import Blueprint
webhook = Blueprint('webhook', __name__)

@webhook.route("/")
def list_of_clothes():
    return "Webhook test"
