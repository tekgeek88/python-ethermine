import json

from typing import Dict


class Statistic(object):

    def __init__(self, time=None, last_seen=None, reported_hashrate=None, average_hashrate=None,
                 current_hashrate=None, valid_shares=None, invalid_shares=None, stale_shares=None, active_workers=None,
                 unpaid=None, unconfirmed=None, coins_per_min=None, usd_per_min=None, btc_per_min=None):
        """
        time    Unix timestamp of the statistic entry
        last_seen    Unix timestamp of when the miner was last seen by the pool
        reported_hashrate    Reported hashrate of the miner in H/s
        average_hashrate Average hashrate of the miner in H/s during the last 24h
        current_hashrate Current hashrate of the miner in H/s
        valid_shares Valid Shares
        invalid_shares   Invalid Shares
        stale_shares Stale Shares
        active_workers   Currently active workers of the miner
        unpaid  Unpaid Balance
        unconfirmed Unconfirmed balance (in base units) of the miner
        coins_per_min Estimated number of coins mined per minute (based on your average hashrate as well as the average block time and difficulty of the network over the last 24 hours.)
        usd_per_min   Estimated number of USD mined per minute (based on your average hashrate as well as the average block time and difficulty of the network over the last 24 hours.)
        btc_per_min   Estimated number of BTC mined per minute (based on your average hashrate as well as the average block time and difficulty of the network over the last 24 hours.)
        """
        self._time = time
        self._last_seen = last_seen
        self._reported_hashrate = reported_hashrate
        self._average_hashrate = average_hashrate
        self._current_hashrate = current_hashrate
        self._valid_shares = valid_shares
        self._invalid_shares = invalid_shares
        self._stale_shares = stale_shares
        self._active_workers = active_workers
        self._unpaid = unpaid
        self._unconfirmed = unconfirmed
        self._coins_per_min = coins_per_min
        self._usd_per_min = usd_per_min
        self._btc_per_min = btc_per_min

    @property
    def time(self) -> str:
        return self._time

    @time.setter
    def time(self, value: str):
        self._time = value

    @property
    def last_seen(self) -> str:
        return self._last_seen

    @last_seen.setter
    def last_seen(self, value: str):
        self._last_seen = value

    @property
    def reported_hashrate(self) -> str:
        return self._reported_hashrate

    @reported_hashrate.setter
    def reported_hashrate(self, value: str):
        self._reported_hashrate = value

    @property
    def average_hashrate(self) -> str:
        return self._average_hashrate

    @average_hashrate.setter
    def average_hashrate(self, value: str):
        self._average_hashrate = value

    @property
    def current_hashrate(self) -> str:
        return self._current_hashrate

    @current_hashrate.setter
    def current_hashrate(self, value: str):
        self._current_hashrate = value

    @property
    def valid_shares(self) -> str:
        return self._valid_shares

    @valid_shares.setter
    def valid_shares(self, value: str):
        self._valid_shares = value

    @property
    def invalid_shares(self) -> str:
        return self._invalid_shares

    @invalid_shares.setter
    def invalid_shares(self, value: str):
        self._invalid_shares = value

    @property
    def stale_shares(self) -> str:
        return self._stale_shares

    @stale_shares.setter
    def stale_shares(self, value: str):
        self._stale_shares = value

    @property
    def active_workers(self) -> str:
        return self._active_workers

    @active_workers.setter
    def active_workers(self, value: str):
        self._active_workers = value

    @property
    def unpaid(self) -> str:
        return self._unpaid

    @unpaid.setter
    def unpaid(self, value: str):
        self._unpaid = value

    @property
    def unconfirmed(self) -> str:
        return self._unconfirmed

    @unconfirmed.setter
    def unconfirmed(self, value: str):
        self._unconfirmed = value

    @property
    def coins_per_min(self) -> str:
        return self._coins_per_min

    @coins_per_min.setter
    def coins_per_min(self, value: str):
        self._coins_per_min = value

    @property
    def usd_per_min(self) -> str:
        return self._usd_per_min

    @usd_per_min.setter
    def usd_per_min(self, value: str):
        self._usd_per_min = value

    @property
    def btc_per_min(self) -> str:
        return self._btc_per_min

    @btc_per_min.setter
    def btc_per_min(self, value: str):
        self._btc_per_min = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        result = {}
        result["time"] = self.time
        result["last_seen"] = self.last_seen
        result["reported_hashrate"] = self.reported_hashrate
        result["average_hashrate"] = self.average_hashrate
        result["current_hashrate"] = self.current_hashrate
        result["valid_shares"] = self.valid_shares
        result["invalid_shares"] = self.invalid_shares
        result["stale_shares"] = self.stale_shares
        result["active_workers"] = self.active_workers
        result["unpaid"] = self.unpaid
        result["unconfirmed"] = self.unconfirmed
        result["coins_per_min"] = self.coins_per_min
        result["usd_per_min"] = self.usd_per_min
        result["btc_per_min"] = self.btc_per_min
        return result

    @staticmethod
    def fromJson(content: Dict[str, str]):
        result = Statistic()
        data = content.get("data", {})
        result.time = data.get("time")
        result.last_seen = data.get("lastSeen")
        result.reported_hashrate = data.get("reportedHashrate")
        result.current_hashrate = data.get("currentHashrate")
        result.valid_shares = data.get("validShares")
        result.invalid_shares = data.get("invalidShares")
        result.stale_shares = data.get("staleShares")
        result.average_hashrate = data.get("averageHashrate")
        result.active_workers = data.get("activeWorkers")
        result.unpaid = data.get("unpaid")
        result.unconfirmed = data.get("unconfirmed")
        result.coins_per_min = data.get("coinsPerMin")
        result.usd_per_min = data.get("usdPerMin")
        result.btc_per_min = data.get("btcPerMin")
        return result
