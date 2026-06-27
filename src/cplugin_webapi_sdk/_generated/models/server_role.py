from enum import Enum

class ServerRole(str, Enum):
    MASTER = "Master"
    SLAVE = "Slave"
    STANDALONE = "StandAlone"

    def __str__(self) -> str:
        return str(self.value)
