from enum import Enum

class EnCommActionMode(str, Enum):
    ALL = "All"
    BUY = "Buy"
    SELL = "Sell"

    def __str__(self) -> str:
        return str(self.value)
