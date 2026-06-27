from enum import Enum

class EnFreeMarginMode(str, Enum):
    LOSS = "Loss"
    NOTUSEPL = "NotUsePL"
    PROFIT = "Profit"
    USEPL = "UsePL"

    def __str__(self) -> str:
        return str(self.value)
