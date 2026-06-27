from enum import Enum

class OrderType(str, Enum):
    BUY = "Buy"
    BUYLIMIT = "BuyLimit"
    BUYSTOP = "BuyStop"
    BUYSTOPLIMIT = "BuyStopLimit"
    CLOSEBY = "CloseBy"
    SELL = "Sell"
    SELLLIMIT = "SellLimit"
    SELLSTOP = "SellStop"
    SELLSTOPLIMIT = "SellStopLimit"

    def __str__(self) -> str:
        return str(self.value)
