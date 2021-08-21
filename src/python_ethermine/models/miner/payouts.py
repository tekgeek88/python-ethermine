import json
from typing import Dict, List
from dataclasses import dataclass, asdict

@dataclass
class Payouts(object):
    data: List = None

    class _Property:
        PAID_ON = "paidOn"  # Unix timestamp of the payout
        START = "start"     # Start block of payout
        END = "end"         # End block of payout
        AMOUNT = "amount"   # Paid amount in base units
        TX_HASH = "txHash"  # Hash of the payout transaction

    def toJson(self):
        return json.dumps(asdict(self))

    @staticmethod
    def fromJson(content: Dict):
        data = content.get("data", {})
        return Payouts(**data)

