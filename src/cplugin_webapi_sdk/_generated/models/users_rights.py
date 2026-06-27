from enum import Enum

class UsersRights(str, Enum):
    APIENABLED = "APIEnabled"
    CONFIRMED = "Confirmed"
    ENABLED = "Enabled"
    EXCLUDEREPORTS = "ExcludeReports"
    EXPERT = "Expert"
    INVESTOR = "Investor"
    NONE = "None"
    OBSOLETE = "Obsolete"
    OTPENABLED = "OTPEnabled"
    PASSWORD = "Password"
    PUSHNOTIFICATION = "PushNotification"
    READONLY = "Readonly"
    REPORTS = "Reports"
    RESETPASS = "ResetPass"
    SPONSOREDHOSTING = "SponsoredHosting"
    TECHNICAL = "Technical"
    TRADEDISABLED = "TradeDisabled"
    TRAILING = "Trailing"

    def __str__(self) -> str:
        return str(self.value)
