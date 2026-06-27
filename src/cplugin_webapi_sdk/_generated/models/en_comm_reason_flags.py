from enum import Enum

class EnCommReasonFlags(str, Enum):
    ALL = "All"
    CLIENT = "Client"
    DEALER = "Dealer"
    EXPERT = "Expert"
    EXTERNALCLIENT = "ExternalClient"
    MOBILE = "Mobile"
    NONE = "None"
    SIGNAL = "Signal"
    WEB = "Web"

    def __str__(self) -> str:
        return str(self.value)
