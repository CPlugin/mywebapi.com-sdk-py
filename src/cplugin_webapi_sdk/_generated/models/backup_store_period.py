from enum import Enum

class BackupStorePeriod(str, Enum):
    MN1 = "Mn1"
    MN3 = "Mn3"
    MN6 = "Mn6"
    Y1 = "Y1"

    def __str__(self) -> str:
        return str(self.value)
