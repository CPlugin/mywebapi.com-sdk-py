from enum import Enum

class EnExecutionMode(str, Enum):
    EXCHANGE = "Exchange"
    INSTANT = "Instant"
    MARKET = "Market"
    REQUEST = "Request"

    def __str__(self) -> str:
        return str(self.value)
