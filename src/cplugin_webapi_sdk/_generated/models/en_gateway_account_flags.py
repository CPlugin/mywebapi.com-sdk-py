from enum import Enum

class EnGatewayAccountFlags(str, Enum):
    NONE = "None"
    QUOTES = "Quotes"

    def __str__(self) -> str:
        return str(self.value)
