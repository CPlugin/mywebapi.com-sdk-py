from enum import Enum

class PreferredCommunication(str, Enum):
    EMAIL = "Email"
    MESSENGER = "Messenger"
    PHONE = "Phone"
    SMS = "SMS"
    UNDEFINED = "Undefined"

    def __str__(self) -> str:
        return str(self.value)
