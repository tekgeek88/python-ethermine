import json
from typing import Dict
from dataclasses import dataclass, asdict

@dataclass
class Statistic(object):
    time: str = None
    last_seen: str = None
    reported_hashrate: str = None
    average_hashrate: str = None
    current_hashrate: str = None
    valid_shares: str = None
    invalid_shares: str = None
    stale_shares: str = None
    active_workers: str = None
    unpaid: str = None
    unconfirmed: str = None
    coins_per_min: str = None
    usd_per_min: str = None
    btc_per_min: str = None
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
   
    def toJson(self):
        return json.dumps(asdict(self))

    @staticmethod
    def fromJson(content: Dict[str, str]):
        data = content.get("data", {})
        return Statistic(**data)
