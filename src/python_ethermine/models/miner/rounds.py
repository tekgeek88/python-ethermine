import json
from typing import Dict, List
from dataclasses import dataclass, asdict

@dataclass
class Rounds(object):
     data: List = None

    class _Property:
        BLOCK = "block"     # Block number of the round
        AMOUNT = "amount"   # Amount in base units allocated to the miner in the round

   def toJson(self):
        return json.dumps(asdict(self))

    @staticmethod
    def fromJson(content: Dict):
        return History(**data)
