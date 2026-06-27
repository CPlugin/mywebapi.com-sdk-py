from enum import Enum

class EnMarginMode(str, Enum):
    EXCHANGEDISCOUNT = "ExchangeDiscount"
    RETAIL = "Retail"
    RETAILHEDGED = "RetailHedged"

    def __str__(self) -> str:
        return str(self.value)
