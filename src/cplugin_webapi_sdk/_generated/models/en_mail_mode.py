from enum import Enum

class EnMailMode(str, Enum):
    DISABLED = "Disabled"
    FULL = "Full"

    def __str__(self) -> str:
        return str(self.value)
