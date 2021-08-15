import json

from typing import Dict


# Array of worker statistics ordered by name ASC
class MinedBlocksStats(object):

    def __init__(self, data=None):
        self._data = data

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
        result = MinedBlocksStats()
        data = content.get("data", {})
        if data is not None and len(data) > 0:
            result.data = []
            for value in data:
                result.data.append(value)
        return result
