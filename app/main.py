import os
from typing import TextIO, Optional, Type


class CleanUpFile:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.file = None

    def __enter__(self) -> TextIO:
        self.file = open(self.file_name)
        return self.file

    def __exit__(self, exc_type: Optional[Type[BaseException]], 
                 exc_val: Optional[BaseException], 
                 exc_tb: Optional[object]) -> None:
        self.file.close()
        os.remove(self.file_name)
