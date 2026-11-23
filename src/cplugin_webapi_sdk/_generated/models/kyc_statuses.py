from enum import Enum

class KYCStatuses(str, Enum):
    APPROVED = "Approved"
    DECLINED = "Declined"
    UNDEFINED = "Undefined"

    def __str__(self) -> str:
        return str(self.value)
