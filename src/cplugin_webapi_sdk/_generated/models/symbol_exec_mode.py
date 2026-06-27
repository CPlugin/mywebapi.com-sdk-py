from enum import Enum

class SymbolExecMode(str, Enum):
    INSTANT = "Instant"
    MARKET = "Market"
    REQUEST = "Request"

    def __str__(self) -> str:
        return str(self.value)
