from enum import Enum

class OrderState(str, Enum):
    CANCELED = "Canceled"
    EXPIRED = "Expired"
    FILLED = "Filled"
    PARTIAL = "Partial"
    PLACED = "Placed"
    REJECTED = "Rejected"
    REQUESTADD = "RequestAdd"
    REQUESTCANCEL = "RequestCancel"
    REQUESTMODIFY = "RequestModify"
    STARTED = "Started"

    def __str__(self) -> str:
        return str(self.value)
