import json
from typing import Dict, List
from dataclasses import dataclass, asdict

@dataclass
class History(object):
    data: List = None

    def toJson(self):
        return json.dumps(asdict(self))

    @staticmethod
    def fromJson(content: Dict):
        return History(**data)
