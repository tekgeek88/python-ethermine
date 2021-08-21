import json
from typing import Dict, List
from dataclasses import dataclass, asdict

@dataclass
class Dashboard(object):
    statistics: List = None 
    workers: List = None
    current_statistics: List = None
    settings: List = None

    def toJson(self):
        return json.dumps(asdict(self))

    @staticmethod
    def fromJson(content: Dict):
        data = content.get("data", {})
        return Dashboard(**data)
