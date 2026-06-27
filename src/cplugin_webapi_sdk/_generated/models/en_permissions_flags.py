from enum import Enum

class EnPermissionsFlags(str, Enum):
    ALL = "All"
    CERTCONFIRM = "CertConfirm"
    ENABLECONNECTION = "EnableConnection"
    FORCEDOTPUSAGE = "ForcedOtpUsage"
    NONE = "None"
    NOTIFYALL = "NotifyAll"
    NOTIFYBALANCES = "NotifyBalances"
    NOTIFYDEALS = "NotifyDeals"
    NOTIFYORDERS = "NotifyOrders"
    REGULATIONPROTECT = "RegulationProtect"
    RESETPASSWORD = "ResetPassword"
    RISKWARNING = "RiskWarning"

    def __str__(self) -> str:
        return str(self.value)
