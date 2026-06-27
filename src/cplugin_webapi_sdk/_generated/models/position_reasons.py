from enum import Enum

class PositionReasons(str, Enum):
    CLIENT = "Client"
    CORPORATEACTION = "CorporateAction"
    DEALER = "Dealer"
    EXPERT = "Expert"
    EXTERNALCLIENT = "ExternalClient"
    EXTERNALSERVICE = "ExternalService"
    GATEWAY = "Gateway"
    MIGRATION = "Migration"
    MOBILE = "Mobile"
    ROLLOVER = "Rollover"
    SETTLEMENT = "Settlement"
    SIGNAL = "Signal"
    SL = "SL"
    SO = "SO"
    SPLIT = "Split"
    SYNC = "Sync"
    TP = "TP"
    TRANSFER = "Transfer"
    VMARGIN = "VMargin"
    WEB = "Web"

    def __str__(self) -> str:
        return str(self.value)
