from enum import Enum

class EnCommissionVolumeType(str, Enum):
    DEAL = "Deal"
    VOLUME = "Volume"

    def __str__(self) -> str:
        return str(self.value)
