from enum import Enum

class EnNewsMode(str, Enum):
    DISABLED = "Disabled"
    FULL = "Full"
    HEADERS = "Headers"

    def __str__(self) -> str:
        return str(self.value)
