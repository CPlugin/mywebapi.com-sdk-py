from enum import Enum

class EnLogType(str, Enum):
    ERRORS = "Errors"
    FAILOVER = "Failover"
    FULL = "Full"
    LOGINS = "Logins"
    SENDMAIL = "SendMail"
    STANDARD = "Standard"
    TRADES = "Trades"
    UPDATER = "Updater"

    def __str__(self) -> str:
        return str(self.value)
