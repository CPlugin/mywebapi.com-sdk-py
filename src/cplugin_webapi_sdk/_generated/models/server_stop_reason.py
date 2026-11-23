from enum import Enum

class ServerStopReason(str, Enum):
    LIVEUPDATE = "LiveUpdate"
    NONE = "None"
    RESTART = "Restart"
    SHUTDOWN = "Shutdown"

    def __str__(self) -> str:
        return str(self.value)
