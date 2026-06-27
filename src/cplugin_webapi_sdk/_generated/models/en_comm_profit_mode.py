from enum import Enum

class EnCommProfitMode(str, Enum):
    ALL = "All"
    LOSS = "Loss"
    PROFIT = "Profit"

    def __str__(self) -> str:
        return str(self.value)
