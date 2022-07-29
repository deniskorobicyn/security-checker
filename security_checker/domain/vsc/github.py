import os
from urllib.request import urlopen
from github import Github, GithubIntegration
fromt github.ContentFile import ContentFile

from security_checker.domain.vsc import VSC

class GithubVSC(VSC):
    def __init__(self, owner, repo_name) -> None:
        app_id = "222372"
        # Read the bot certificate
        with open(
                os.path.normpath(os.path.expanduser("./secrets/private-key.pem")),
                'r'
        ) as cert_file:
            app_key = cert_file.read()

        # Create an GitHub integration instance
        git_integration = GithubIntegration(
            app_id,
            app_key,
        )
        self.github = Github(
            login_or_token=git_integration.get_access_token(
                git_integration.get_installation(owner, repo_name).id
            ).token
        )
        self.repo = self.github.get_repo(f"{owner}/{repo_name}")

    def fetch_poetry(self) -> ContentFile:
        self.repo.get_contents("poetry.lock")

    def fetch_diff(self, head, base) -> str:
        comparasion = self.repo.compare(head, base)
        diff_url = comparasion.diff_url
        return urlopen(diff_url).read().decode('utf-8')

    def update_status(self, status) -> None:
        self.repo.get_commit(sha=self.sha).create_status(
            state=status,
            target_url="https://FooCI.com",
            description="FooCI is building",
            context="ci/FooCI"
        )