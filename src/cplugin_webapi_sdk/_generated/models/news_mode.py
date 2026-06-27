from enum import Enum

class NewsMode(str, Enum):
    FULL = "Full"
    NO = "No"
    TOPICS = "Topics"

    def __str__(self) -> str:
        return str(self.value)
