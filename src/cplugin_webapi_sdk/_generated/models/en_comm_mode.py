from enum import Enum

class EnCommMode(str, Enum):
    AGENT = "Agent"
    FEE = "Fee"
    STANDARD = "Standard"

    def __str__(self) -> str:
        return str(self.value)
