import json
from typing import Dict
from dataclasses import dataclass, asdict


# Array of worker statistics ordered by name ASC
@dataclass
class BasicPoolStats(object):
    mined_blocks: any = None
    pool_stats: any = None
    price: any = None

    def toJson(self):
        return json.dumps(asdict(self))

    @staticmethod
    def fromJson(content: Dict):
        result = BasicPoolStats()
        data = content.get("data", {})
        return BasicPoolStats(**data)
