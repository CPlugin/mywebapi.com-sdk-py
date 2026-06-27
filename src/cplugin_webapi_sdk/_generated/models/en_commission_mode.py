from enum import Enum

class EnCommissionMode(str, Enum):
    MONEYDEPOSIT = "MoneyDeposit"
    MONEYSPECIFIED = "MoneySpecified"
    MONEYSYMBOLBASE = "MoneySymbolBase"
    MONEYSYMBOLMARGIN = "MoneySymbolMargin"
    MONEYSYMBOLPROFIT = "MoneySymbolProfit"
    PERCENT = "Percent"
    PERCENTPROFIT = "PercentProfit"
    PIPS = "Pips"

    def __str__(self) -> str:
        return str(self.value)
