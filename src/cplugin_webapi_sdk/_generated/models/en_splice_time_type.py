from enum import Enum

class EnSpliceTimeType(str, Enum):
    EXPIRATION = "Expiration"

    def __str__(self) -> str:
        return str(self.value)
