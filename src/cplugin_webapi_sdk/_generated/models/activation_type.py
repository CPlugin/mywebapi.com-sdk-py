from enum import Enum

class ActivationType(str, Enum):
    NONE = "None"
    PENDING = "Pending"
    PENDINGROLLBACK = "PendingRollback"
    SL = "SL"
    SLROLLBACK = "SLRollback"
    STOPOUT = "Stopout"
    STOPOUTROLLBACK = "StopOutRollback"
    TP = "TP"
    TPROLLBACK = "TPRollback"

    def __str__(self) -> str:
        return str(self.value)
