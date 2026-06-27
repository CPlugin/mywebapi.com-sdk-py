from enum import Enum

class PositionActions(str, Enum):
    BUY = "Buy"
    SELL = "Sell"

    def __str__(self) -> str:
        return str(self.value)
