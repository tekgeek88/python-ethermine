import json

from typing import Dict


# Array of worker statistics ordered by name ASC
class IndividualWorkerStats(object):

    def __init__(self, time=None, last_seen=None, reported_hashrate=None, average_hashrate=None, current_hashrate=None,
                 valid_shares=None, invalid_shares=None, stale_shares=None):
        self._time = time
        self._last_seen = last_seen
        self._reported_hashrate = reported_hashrate
        self._average_hashrate = average_hashrate
        self._current_hashrate = current_hashrate
        self._valid_shares = valid_shares
        self._invalid_shares = invalid_shares
        self._stale_shares = stale_shares

    @property
    def time(self) -> any:
        return self._time

    @time.setter
    def time(self, value: any):
        self._time = value

    @property
    def last_seen(self) -> any:
        return self._last_seen

    @last_seen.setter
    def last_seen(self, value: any):
        self._last_seen = value

    @property
    def reported_hashrate(self) -> any:
        return self._reported_hashrate

    @reported_hashrate.setter
    def reported_hashrate(self, value: any):
        self._reported_hashrate = value

    @property
    def average_hashrate(self) -> any:
        return self._average_hashrate

    @average_hashrate.setter
    def average_hashrate(self, value: any):
        self._average_hashrate = value

    @property
    def current_hashrate(self) -> any:
        return self._current_hashrate

    @current_hashrate.setter
    def current_hashrate(self, value: any):
        self._current_hashrate = value

    @property
    def valid_shares(self) -> any:
        return self._valid_shares

    @valid_shares.setter
    def valid_shares(self, value: any):
        self._valid_shares = value

    @property
    def invalid_shares(self) -> any:
        return self._invalid_shares

    @invalid_shares.setter
    def invalid_shares(self, value: any):
        self._invalid_shares = value

    @property
    def stale_shares(self) -> any:
        return self._stale_shares

    @stale_shares.setter
    def stale_shares(self, value: any):
        self._stale_shares = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        result = {}
        result["data"] = self.data
        return result

    @staticmethod
    def fromJson(content: Dict):
        result = IndividualWorkerStats()
        data = content.get("data", {})

        if 'time' in data:
            result.time = data['time']
        if 'lastSeen' in data:
            result.last_seen = data['lastSeen']
        if 'reportedHashrate' in data:
            result.reported_hashrate = data['reportedHashrate']
        if 'averageHashrate' in data:
            result.average_hashrate = data['averageHashrate']
        if 'currentHashrate' in data:
            result.current_hashrate = data['currentHashrate']
        if 'validShares' in data:
            result.valid_shares = data['validShares']
        if 'invalidShares' in data:
            result.invalid_shares = data['invalidShares']
        if 'staleShares' in data:
            result.stale_shares = data['staleShares']

        return result
