from dataclasses import dataclass
import os

@dataclass
class data:
    commit: str
    remote_link: str
    branch: str
    path_local: str = os.path.abspath(__file__)
