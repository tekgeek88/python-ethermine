import json

from typing import Dict


# Array of worker statistics ordered by name ASC
class NetworkStatistics(object):

    def __init__(self, time=None, block_time=None, difficulty=None, hashrate=None, usd=None, btc=None):
        self._time = time
        self._block_time = block_time
        self._difficulty = difficulty
        self._hashrate = hashrate
        self._usd = usd
        self._btc = btc

    @property
    def time(self) -> any:
        return self._time

    @time.setter
    def time(self, value: any):
        self._time = value

    @property
    def block_time(self) -> any:
        return self._block_time

    @block_time.setter
    def block_time(self, value: any):
        self._block_time = value

    @property
    def difficulty(self) -> any:
        return self._difficulty

    @difficulty.setter
    def difficulty(self, value: any):
        self._difficulty = value

    @property
    def hashrate(self) -> any:
        return self._hashrate

    @hashrate.setter
    def hashrate(self, value: any):
        self._hashrate = value

    @property
    def usd(self) -> any:
        return self._usd

    @usd.setter
    def usd(self, value: any):
        self._usd = value

    @property
    def btc(self) -> any:
        return self._btc

    @btc.setter
    def btc(self, value: any):
        self._btc = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        result = {}
        result["time"] = self.time
        result["block_time"] = self.block_time
        result["difficulty"] = self.difficulty
        result["hashrate"] = self.hashrate
        result["usd"] = self.usd
        result["btc"] = self.btc
        return result

    @staticmethod
    def fromJson(content: Dict):
        result = NetworkStatistics()
        data = content.get("data", {})
        if data is not None and len(data) > 0:
            if 'time' in data:
                result.time = data['time']
            if 'blockTime' in data:
                result.block_time = data['blockTime']
            if 'difficulty' in data:
                result.difficulty = data['difficulty']
            if 'hashrate' in data:
                result.hashrate = data['hashrate']
            if 'usd' in data:
                result.usd = data['usd']
            if 'btc' in data:
                result.btc = data['btc']
        return result
