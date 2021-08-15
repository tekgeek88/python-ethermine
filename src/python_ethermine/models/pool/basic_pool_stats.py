import json

from typing import Dict


# Array of worker statistics ordered by name ASC
class BasicPoolStats(object):

    def __init__(self, mined_blocks=None, pool_stats=None, price=None):
        self._mined_blocks = mined_blocks
        self._pool_stats = pool_stats
        self._price = price


    @property
    def mined_blocks(self) -> any:
        return self._mined_blocks

    @mined_blocks.setter
    def mined_blocks(self, value: any):
        self._mined_blocks = value

    @property
    def pool_stats(self) -> any:
        return self._pool_stats

    @pool_stats.setter
    def pool_stats(self, value: any):
        self._pool_stats = value

    @property
    def price(self) -> any:
        return self._price

    @price.setter
    def price(self, value: any):
        self._price = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        result = {}
        result["mined_blocks"] = self.mined_blocks
        result["pool_stats"] = self.pool_stats
        result["price"] = self.price
        return result

    @staticmethod
    def fromJson(content: Dict):
        result = BasicPoolStats()
        data = content.get("data", {})

        if data is not None and len(data) > 0:

            if "minedBlocks" in data:
                mined_blocks = data.get('minedBlocks')
                if mined_blocks is not None and len(mined_blocks) > 0:
                    result.mined_blocks = []
                    for value in mined_blocks:
                        result.mined_blocks.append(value)

            if "poolStats" in data:
                pool_stats = data.get('poolStats')
                if pool_stats is not None and len(pool_stats) > 0:
                    result.pool_stats = {}
                    for key, value in pool_stats.items():
                        result.pool_stats[key] = value

            if "price" in data:
                price = data.get('price')
                if price is not None and len(price) > 0:
                    result.price = {}
                    for key, value in price.items():
                        result.price[key] = value

        return result
