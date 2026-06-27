from enum import Enum

class EnManagerLimit(str, Enum):
    ALL = "All"
    MONTHS1 = "Months1"
    MONTHS3 = "Months3"
    MONTHS6 = "Months6"
    YEAR1 = "Year1"
    YEAR2 = "Year2"
    YEAR3 = "Year3"

    def __str__(self) -> str:
        return str(self.value)
