import os

class File:
    def __init__(self, filepath: str):
        self.path = filepath
        self.name = os.path.basename(filepath)