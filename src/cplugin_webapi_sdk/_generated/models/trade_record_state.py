from enum import Enum

class TradeRecordState(str, Enum):
    CLOSEDBY = "ClosedBy"
    CLOSEDNORMAL = "ClosedNormal"
    CLOSEDPART = "ClosedPart"
    DELETED = "Deleted"
    OPENNORMAL = "OpenNormal"
    OPENREMAND = "OpenRemand"
    OPENRESTORED = "OpenRestored"

    def __str__(self) -> str:
        return str(self.value)
