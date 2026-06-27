from enum import Enum

class EnCalcMode(str, Enum):
    CFD = "Cfd"
    CFDINDEX = "CfdIndex"
    CFDLEVERAGE = "CfdLeverage"
    EXCHBONDS = "ExchBonds"
    EXCHBONDSMOEX = "ExchBondsMoex"
    EXCHFUTURES = "ExchFutures"
    EXCHFUTURESFORTS = "ExchFuturesForts"
    EXCHOPTIONS = "ExchOptions"
    EXCHOPTIONSMARGIN = "ExchOptionsMargin"
    EXCHSTOCKS = "ExchStocks"
    EXCHSTOCKSMOEX = "ExchStocksMoex"
    FOREX = "Forex"
    FOREXNOLEVERAGE = "ForexNoLeverage"
    FUTURES = "Futures"
    SERVCOLLATERAL = "ServCollateral"

    def __str__(self) -> str:
        return str(self.value)
