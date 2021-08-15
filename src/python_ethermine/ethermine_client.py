from .base_client import BaseClient
from .controllers.miner import Miner
from .controllers.worker import Worker
from .controllers.pool import Pool


class EthermineClient:

    def __init__(self, url: str = "https://api.ethermine.org"):
        self._base_client = BaseClient(url)
        self._miner = Miner(self._base_client)
        self._worker = Worker(self._base_client)
        self._pool = Pool(self._base_client)

    @property
    def url(self) -> str:
        return self._base_client.url

    @property
    def base_client(self) -> BaseClient:
        return self._base_client

    @property
    def Miner(self) -> Miner:
        return self._miner

    @property
    def Worker(self) -> Worker:
        return self._worker

    @property
    def Pool(self) -> Pool:
        return self._pool
