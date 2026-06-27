from enum import Enum

class DealReason(str, Enum):
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
    SL = "Sl"
    SO = "So"
    SPLIT = "Split"
    SYNC = "Sync"
    TP = "Tp"
    TRANSFER = "Transfer"
    VMARGIN = "VMargin"
    WEB = "Web"

    def __str__(self) -> str:
        return str(self.value)
