from __future__ import annotations

import os
from typing import Optional, Type, TextIO


class CleanUpFile:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.file = None

    def __enter__(self) -> TextIO:
        try:
            self.file = open(self.file_name, "r")
        except FileNotFoundError:
            print(f"Error: File '{self.file_name}' does not exist.")
            raise
        except PermissionError:
            print(f"Error: Permission denied for file '{self.file_name}'.")
            raise
        except IOError as e:
            print(f"An I/O error occurred: {e}")
            raise
        return self.file

    def __exit__(self, exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[BaseException],
                 exc_tb: Optional[object]) -> None:
        try:
            if self.file:
                self.file.close()  # Закриваємо файл
            os.remove(self.file_name)  # Видаляємо файл
        except FileNotFoundError:
            print(f"Error: File '{self.file_name}' was not "
                  f"found during deletion.")
        except PermissionError:
            print(f"Error: Permission denied when trying "
                  f"to delete '{self.file_name}'.")
        except IOError as e:
            print(f"An I/O error occurred while deleting the file: {e}")
