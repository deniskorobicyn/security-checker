import os
from security_checker.domain.diff_packages import DiffPackages

def test_fetch():
    with open(
        os.path.normpath(os.path.expanduser("./tests/fixtures/github_diff.diff")),
        'r'
    ) as diff_file:
        test_diff = diff_file.read()
    with open(
        os.path.normpath(os.path.expanduser("./tests/fixtures/poetry.lock")),
        'r'
    ) as poetry_file:
        poetry_data = poetry_file.read()
    packages = DiffPackages.parse(test_diff, poetry_data)

    assert packages.new_packages == ['unidiff']
