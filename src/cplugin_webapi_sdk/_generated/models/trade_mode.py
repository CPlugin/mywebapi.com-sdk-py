from enum import Enum

class TradeMode(str, Enum):
    CLOSE = "Close"
    FULL = "Full"
    NO = "No"

    def __str__(self) -> str:
        return str(self.value)
