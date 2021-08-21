import json
from typing import Dict, List
from dataclasses import dataclass, asdict


# Array of worker statistics ordered by name ASC
@dataclass
class MinedBlocksStats(object):
    data: List = None

    def toJson(self):
        return json.dumps(asdict(self))

    @staticmethod
    def fromJson(content: Dict):
        result = MinedBlocksStats()
        data = content.get("data", {})
        return MinedBlocksStats(**data)
