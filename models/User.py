from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    id: int
    name: str
    status: str
    no_of_followers: Optional[int] = None

    def print(self):
        print(str(self.id) + " : " + self.name + " --> " + self.status)