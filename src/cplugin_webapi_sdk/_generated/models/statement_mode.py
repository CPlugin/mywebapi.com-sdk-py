from enum import Enum

class StatementMode(str, Enum):
    ENDDAY = "EndDay"
    STARTDAY = "StartDay"

    def __str__(self) -> str:
        return str(self.value)
