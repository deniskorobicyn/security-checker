from security_checker.domain.dir.temp_repo import TempRepo
from security_checker.domain.dir.file import File
from security_checker.domain.checker import Checker


def test_test_audit():
    temp_repo = TempRepo()
    package_json = File("./tests/fixtures/package.json")
    package_lock =File("./tests/fixtures/package-lock.json")
    temp_repo.populate([package_json, package_lock])
    checker = Checker(temp_repo)

    assert checker.run() == 1
