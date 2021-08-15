import json

from typing import Dict


class Settings(object):
    class _Property:
        EMAIL = "email"  # Masked Email address of the miner
        MONITOR = "monitor"  # Monitoring enabled (1 for yes, 0 for no)
        MIN_PAYOUT = "minPayout"  # Minimum payout amount defined by the miner in base units
        IP = "ip"  # Masked IP address of one randomly selected worker

    def __init__(self, email: any = None, monitor: any = None, min_payout: any = None, ip: any = None):
        self._email = email
        self._monitor = monitor
        self._min_payout = min_payout
        self._ip = ip

    @property
    def email(self) -> any:
        return self._email

    @email.setter
    def email(self, value: any):
        self._email = value

    @property
    def monitor(self) -> any:
        return self._monitor

    @monitor.setter
    def monitor(self, value: any):
        self._monitor = value

    @property
    def min_payout(self) -> any:
        return self._min_payout

    @min_payout.setter
    def min_payout(self, value: any):
        self._min_payout = value

    @property
    def ip(self) -> any:
        return self._ip

    @ip.setter
    def ip(self, value: any):
        self._ip = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        result = {}
        result["email"] = self.email
        result["monitor"] = self.monitor
        result["min_payout"] = self.min_payout
        result["ip"] = self.ip
        return result

    @staticmethod
    def fromJson(content: Dict):
        result = Settings()
        data = content.get("data", {})
        result.email = data.get(result._Property.EMAIL)
        result.monitor = data.get(result._Property.MONITOR)
        result.min_payout = data.get(result._Property.MIN_PAYOUT)
        result.ip = data.get(result._Property.IP)
        return result
