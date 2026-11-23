from enum import Enum

class ClientStatuses(str, Enum):
    ACTIVE = "Active"
    APPLICATIONCOMPLETED = "ApplicationCompleted"
    APPLICATIONINCOMPLETE = "ApplicationIncomplete"
    APPLICATIONINFORMATION = "ApplicationInformation"
    APPLICATIONREJECTED = "ApplicationRejected"
    APPROVED = "Approved"
    CLOSED = "Closed"
    FUNDED = "Funded"
    INACTIVE = "Inactive"
    NOTINTERESTED = "NotInterested"
    REGISTERED = "Registered"
    SUSPENDED = "Suspended"
    TERMINATED = "Terminated"
    UNREGISTERED = "Unregistered"

    def __str__(self) -> str:
        return str(self.value)
