from enum import Enum

class EnTradeRightsFlags(str, Enum):
    ALL = "All"
    DEALCOST = "DealCost"
    DEFAULT = "Default"
    EXPERTS = "Experts"
    EXPIRATION = "Expiration"
    FIFOCLOSE = "FifoClose"
    HEDGEPROHIBIT = "HedgeProhibit"
    NONE = "None"
    SIGNALSALL = "SignalsAll"
    SIGNALSOWN = "SignalsOwn"
    SOCOMPENSATION = "SOCompensation"
    SOCOMPENSATIONCREDIT = "SOCompensationCredit"
    SOFULLYHEDGED = "SOFullyHedged"
    SWAPS = "Swaps"
    TRAILING = "Trailing"

    def __str__(self) -> str:
        return str(self.value)
