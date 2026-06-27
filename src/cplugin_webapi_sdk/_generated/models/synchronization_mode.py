from enum import Enum

class SynchronizationMode(str, Enum):
    ADD = "Add"
    DELETE = "Delete"
    INSERT = "Insert"
    LAST = "Last"
    UPDATE = "Update"

    def __str__(self) -> str:
        return str(self.value)
