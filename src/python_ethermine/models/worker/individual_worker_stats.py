import json
from typing import Dict
from dataclasses import dataclass, asdict

# Array of worker statistics ordered by name ASC
@dataclass
class IndividualWorkerStats(object):
    time: any = None
    last_seen: any = None
    reported_hashrate: any = None
    average_hashrate: any = None
    current_hashrate: any = None
    valid_shares: any = None
    invalid_shares: any = None
    stale_shares: any = None

    def toJson(self):
        return json.dumps(asdict(self))

    @staticmethod
    def fromJson(content: Dict):
        result = IndividualWorkerStats()
        data = content.get("data", {})
        return IndividualWorkerStats(**data)
