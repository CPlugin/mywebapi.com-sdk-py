from enum import Enum

class EnReportsFlags(str, Enum):
    ALL = "All"
    EMAIL = "Email"
    NONE = "None"
    STATEMENTS = "Statements"
    SUPPORT = "Support"

    def __str__(self) -> str:
        return str(self.value)
