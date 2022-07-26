import os
from typing import List
from github import Github, GithubIntegration
from github.Comparison import Comparison
from security_checker.domain.config import Config

from security_checker.domain.vsc import VSC


class Github(VSC):
    def __init__(self, owner, repo_name) -> None:
        config = Config._instance
        app_id = config.github.app_id
        # Read the bot certificate
        with open(
                os.path.normpath(os.path.expanduser(config.github.pem_path)),
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
        self.repo = self.github.get_repo(f"{self.owner}/{self.repo_name}")
    )


    def fetch_diff(self, head, base) -> Comparison:
        return self.repo.compare(head, base)

    def update_status(self, status) -> None:
        self.repo.get_commit(sha=self.sha).create_status(
            state=status,
            target_url="https://FooCI.com",
            description="FooCI is building",
            context="ci/FooCI"
        )