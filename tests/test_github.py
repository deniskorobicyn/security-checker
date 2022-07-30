import os
from security_checker.domain.vsc.github import GithubVSC

def test_fetch():
    github = GithubVSC("deniskorobicyn", "security-checker")
    result = github.fetch_diff("29b4a63d7b", "34042d7ba801fe")

    with open(
        os.path.normpath(os.path.expanduser("./tests/fixtures/github_diff.diff")),
        'r'
    ) as diff_file:
            test_diff = diff_file.read()

    assert result == test_diff

def test_fetch_poetry():
    github = GithubVSC("deniskorobicyn", "security-checker")
    result = github.fetch_poetry("3e48df0d9ca737")

    with open(
        os.path.normpath(os.path.expanduser("./tests/fixtures/poetry.lock")),
        'r'
    ) as poetry_file:
            poetry = poetry_file.read()

    assert result.decoded_content.decode("utf-8") == poetry