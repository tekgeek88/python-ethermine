import json
from typing import Dict
from dataclasses import dataclass, asdict

@dataclass
class Settings(object):

    email: any = None
    monitor: any = None
    min_payout: any = None 
    ip: any = None 

    class _Property:
        EMAIL = "email"  # Masked Email address of the miner
        MONITOR = "monitor"  # Monitoring enabled (1 for yes, 0 for no)
        MIN_PAYOUT = "minPayout"  # Minimum payout amount defined by the miner in base units
        IP = "ip"  # Masked IP address of one randomly selected worker

    def toJson(self):
        return json.dumps(asdict(self))

    @staticmethod
    def fromJson(content: Dict):
        data = content.get("data", {})
        return Settings(**data)
