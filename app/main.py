import os
class CleanUpFile:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.file = None

    def __enter__(self):
        self.file = open(self.file_name)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        os.remove(self.file_name)
