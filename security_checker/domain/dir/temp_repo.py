import shutil
import os
from security_checker.domain.dir.file import File
from typing import List

class TempRepo:
    def populate(self, files: List[File]):
        for file in files:
            shutil.copy2(file.path, f"{self.folder()}/{file.name}")

    def folder(self):
        # TODO: use tempdit
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, '../../../temp/')
        return filename