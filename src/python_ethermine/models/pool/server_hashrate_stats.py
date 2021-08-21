import json
from typing import Dict
from dataclasses import dataclass, asdict


# Array of worker statistics ordered by name ASC
@dataclass
class ServerHashrateStats(object):
    data: any = None

    def toJson(self):
        return json.dumps(asdict(self))

    @staticmethod
    def fromJson(content: Dict):
        result = ServerHashrateStats()
        data = content.get("data", {})
        return ServerHashrateStats(**data)
