from enum import Enum

class EnStopOutMode(str, Enum):
    MONEY = "Money"
    PERCENT = "Percent"

    def __str__(self) -> str:
        return str(self.value)
