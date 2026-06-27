from enum import Enum

class TradeActivationFlags(str, Enum):
    ALL = "All"
    NOEXPIRATION = "NoExpiration"
    NOLIMIT = "NoLimit"
    NONE = "None"
    NOSL = "NoSL"
    NOSLIMIT = "NoSLimit"
    NOSO = "NoSO"
    NOSTOP = "NoStop"
    NOTP = "NoTP"

    def __str__(self) -> str:
        return str(self.value)
