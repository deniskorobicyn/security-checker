from flask import Blueprint, request
from security_checker.domain.github import Github
from security_checker.domain.checker import Checker
webhook = Blueprint('webhook', __name__)

@webhook.route("/", methods=['POST'])
def webhook_process():
    payload = request.json
    vcs = VCS.parse(payload)
    vcs.update_status('pending')

    changes = vcs.changes()
    checker = Checker()
    result = checker.run(changes)
    if result.success:
        vcs.update_status('success')

    vcs.update_result(result)
    return "ok"
