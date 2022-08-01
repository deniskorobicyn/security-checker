import subprocess
from security_checker.domain.dir.temp_repo import TempRepo

class Checker:
    def __init__(self, temp_repo: TempRepo) -> None:
        self.temp_repo = temp_repo

    def run(self) -> int:
        subprocess.run(f"cd {self.temp_repo.folder()}")
        subprocess.run("npm install")
        result = subprocess.run("npm audit")

        return result.code