from enum import Enum

class WebApiErrorCode(str, Enum):
    BUSY = "Busy"
    FORBIDDEN = "Forbidden"
    INTERNAL = "Internal"
    MT4ERROR = "MT4Error"
    MT5ERROR = "MT5Error"
    NOCONNECT = "NoConnect"
    NOTFOUND = "NotFound"
    OK = "Ok"
    OUTCOMEUNKNOWN = "OutcomeUnknown"
    TIMEOUT = "Timeout"
    VALIDATION = "Validation"

    def __str__(self) -> str:
        return str(self.value)
