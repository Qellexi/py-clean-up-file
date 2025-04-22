import os
from typing import TextIO


class CleanUpFile:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.file = None

    def __enter__(self) -> TextIO:
        self.file = open(self.file_name)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.file.close()
        os.remove(self.file_name)
