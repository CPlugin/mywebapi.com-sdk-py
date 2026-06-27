from enum import Enum

class EnSwapMode(str, Enum):
    BYGROUPCURRENCY = "ByGroupCurrency"
    BYINTERESTCURRENT = "ByInterestCurrent"
    BYINTERESTOPEN = "ByInterestOpen"
    BYMARGINCURRENCY = "ByMarginCurrency"
    BYPOINTS = "ByPoints"
    BYPROFITCURRENCY = "ByProfitCurrency"
    BYSYMBOLCURRENCY = "BySymbolCurrency"
    DISABLED = "Disabled"
    REOPENBYBID = "ReopenByBid"
    REOPENBYCLOSEPRICE = "ReopenByClosePrice"

    def __str__(self) -> str:
        return str(self.value)
