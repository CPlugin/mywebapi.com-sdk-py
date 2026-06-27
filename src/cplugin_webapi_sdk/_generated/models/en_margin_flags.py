from enum import Enum

class EnMarginFlags(str, Enum):
    ALL = "All"
    CHECKPROCESS = "CheckProcess"
    CHECKSLTP = "CheckSLTP"
    EXCLUDEPL = "ExcludePl"
    HEDGELARGELEG = "HedgeLargeLeg"
    NONE = "None"
    RECALCRATES = "RecalcRates"

    def __str__(self) -> str:
        return str(self.value)
