from enum import Enum

class MonthlyStatementMode(str, Enum):
    ENDMONTH = "EndMonth"
    STARTMONTH = "StartMonth"

    def __str__(self) -> str:
        return str(self.value)
