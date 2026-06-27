from enum import Enum

class GroupRights(str, Enum):
    ADVISOR = "Advisor"
    EXPIRATION = "Expiration"
    FORCEDOTPUSAGE = "ForcedOTPUsage"
    RISKWARNING = "RiskWarning"
    SIGNALALL = "SignalAll"
    SIGNALS = "Signals"
    SIGNALSOWN = "SignalsOwn"
    TRAILING = "Trailing"

    def __str__(self) -> str:
        return str(self.value)
