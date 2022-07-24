from flask import Blueprint, request
webhook = Blueprint('webhook', __name__)

@webhook.route("/", methods=['POST'])
def webhook_process():
    payload = request.json
    print(payload)
    return "ok"
