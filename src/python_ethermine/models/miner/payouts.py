import json

from typing import Dict


class Payouts(object):

    class _Property:
        PAID_ON = "paidOn"  # Unix timestamp of the payout
        START = "start"     # Start block of payout
        END = "end"         # End block of payout
        AMOUNT = "amount"   # Paid amount in base units
        TX_HASH = "txHash"  # Hash of the payout transaction

    def __init__(self, data=None):
        self.data = data

    @property
    def data(self) -> list:
        return self._data

    @data.setter
    def data(self, value: list):
        self._data = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        result = {}
        result["data"] = self.data
        return result

    @staticmethod
    def fromJson(content: Dict):
        result = Payouts()
        data = content.get("data", {})

        if data is not None and len(data) > 0:
            result.data = []
            for value in data:
                result.data.append(value)

        return result
