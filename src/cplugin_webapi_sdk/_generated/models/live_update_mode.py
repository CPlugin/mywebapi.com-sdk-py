from enum import Enum

class LiveUpdateMode(str, Enum):
    ALL = "All"
    NO = "No"
    NOSERVER = "NoServer"

    def __str__(self) -> str:
        return str(self.value)
