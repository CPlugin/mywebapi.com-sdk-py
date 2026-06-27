from enum import Enum

class EnTransferMode(str, Enum):
    TRANSFERMODEDISABLED = "TransferModeDisabled"
    TRANSFERMODEGROUP = "TransferModeGroup"
    TRANSFERMODENAME = "TransferModeName"
    TRANSFERMODENAMEGROUP = "TransferModeNameGroup"

    def __str__(self) -> str:
        return str(self.value)
