from enum import Enum

class TradeCommand(str, Enum):
    BALANCE = "Balance"
    BUY = "Buy"
    BUYLIMIT = "BuyLimit"
    BUYSTOP = "BuyStop"
    CREDIT = "Credit"
    SELL = "Sell"
    SELLLIMIT = "SellLimit"
    SELLSTOP = "SellStop"

    def __str__(self) -> str:
        return str(self.value)
