from enum import Enum

class TradeRecordReason(str, Enum):
    API = "API"
    CLIENT = "Client"
    DEALER = "Dealer"
    EXPERT = "Expert"
    GATEWAY = "Gateway"
    MOBILE = "Mobile"
    SIGNAL = "Signal"
    WEB = "Web"

    def __str__(self) -> str:
        return str(self.value)
