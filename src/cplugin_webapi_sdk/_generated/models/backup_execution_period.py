from enum import Enum

class BackupExecutionPeriod(str, Enum):
    D1 = "D1"
    H1 = "H1"
    H4 = "H4"

    def __str__(self) -> str:
        return str(self.value)
