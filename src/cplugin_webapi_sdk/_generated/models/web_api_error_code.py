from enum import Enum

class WebApiErrorCode(str, Enum):
    FORBIDDEN = "Forbidden"
    INTERNAL = "Internal"
    MT4ERROR = "MT4Error"
    MT5ERROR = "MT5Error"
    NOCONNECT = "NoConnect"
    NOTFOUND = "NotFound"
    OK = "Ok"
    VALIDATION = "Validation"

    def __str__(self) -> str:
        return str(self.value)
