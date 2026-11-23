from enum import Enum

class EmploymentIndustry(str, Enum):
    AGRICULTURE = "Agriculture"
    COMMUNICATION = "Communication"
    CONSTRUCTION = "Construction"
    EDUCATION = "Education"
    ENGINEERING = "Engineering"
    GOVERNMENT = "Government"
    HEALTHCARE = "Healthcare"
    IT = "IT"
    MANAGEMENT = "Management"
    MANUFACTURING = "Manufacturing"
    MARKETING = "Marketing"
    NONE = "None"
    OTHER = "Other"
    SCIENCE = "Science"
    SECURITY = "Security"
    TOURISM = "Tourism"
    TRANSPORT = "Transport"

    def __str__(self) -> str:
        return str(self.value)
