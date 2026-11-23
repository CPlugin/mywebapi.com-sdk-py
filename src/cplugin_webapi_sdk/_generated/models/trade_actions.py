from enum import Enum

class TradeActions(str, Enum):
    ACTIVATE = "Activate"
    ACTIVATESL = "ActivateSL"
    ACTIVATESTOPLIMIT = "ActivateStopLimit"
    ACTIVATETP = "ActivateTP"
    CLOSEBY = "CloseBy"
    DEALERBALANCE = "DealerBalance"
    DEALERCLOSEBY = "DealerCloseBy"
    DEALERORDACTIVATE = "DealerOrdActivate"
    DEALERORDMODIFY = "DealerOrdModify"
    DEALERORDPENDING = "DealerOrdPending"
    DEALERORDREMOVE = "DealerOrdRemove"
    DEALERORDSLIMIT = "DealerOrdSLimit"
    DEALERPOSEXECUTE = "DealerPosExecute"
    DEALERPOSMODIFY = "DealerPosModify"
    END = "End"
    EXCHANGE = "Exchange"
    EXPIRATION = "Expiration"
    INSTANT = "Instant"
    MARKET = "Market"
    MODIFY = "Modify"
    PENDING = "Pending"
    PRICE = "Price"
    REMOVE = "Remove"
    REQUEST = "Request"
    SLTP = "SLTP"
    STOPOUTORDER = "StopOutOrder"
    STOPOUTPOSITION = "StopOutPosition"
    TRANSFER = "Transfer"

    def __str__(self) -> str:
        return str(self.value)
