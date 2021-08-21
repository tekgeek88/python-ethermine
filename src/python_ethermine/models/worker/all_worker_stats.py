import json
from typing import Dict, List
from dataclasses import dataclass, asdict

@dataclass


# Array of worker statistics ordered by name ASC
class AllWorkerStats(object):
    data: List = None

    def toJson(self):
        return json.dumps(asdict(self))

    @staticmethod
    def fromJson(content: Dict):
        return AllWorkerStats(**data)
