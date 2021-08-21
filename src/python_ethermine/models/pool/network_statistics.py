import json
from typing import Dict
from dataclasses import dataclass, asdict


# Array of worker statistics ordered by name ASC
@dataclass
class NetworkStatistics(object):
    time: any = None
    block_time: any = None
    difficulty: any = None
    hashrate: any = None
    usd: any = None
    btc: any = None
    
    def toJson(self):
        return json.dumps(asdict(self))

    @staticmethod
    def fromJson(content: Dict):
        result = NetworkStatistics()
        data = content.get("data", {})
        return NetworkStatistics(**data)
