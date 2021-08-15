from ..base_client import BaseClient
from ..models.worker.all_worker_stats import AllWorkerStats
from ..models.worker.individual_historical_worker_stats import IndividualHistoricalWorkerStats
from ..models.worker.individual_worker_stats import IndividualWorkerStats


class Worker(object):
    def __init__(self, client: BaseClient):
        self._url = client.url
        self._base_client = client
        self._setPaths()

    def get_all_worker_stats(self, address: str) -> AllWorkerStats:
        if address is None:
            raise TypeError

        response = self._base_client.request(
            method='get',
            url=self.__all_worker_stats_path.format(address=address)
        )
        self._base_client.check_response(response, f'Failed to get All Worker Stats, {address}.')
        result = AllWorkerStats.fromJson(response.json())
        return result

    def get_individual_worker_stats(self, address: str, worker: str) -> IndividualWorkerStats:
        if address is None or worker is None:
            raise TypeError

        response = self._base_client.request(
            method='get',
            url=self.__individual_worker_stats_path.format(address=address, worker=worker)
        )
        self._base_client.check_response(response, f'Failed to get Individual Worker Stats, {address}.')
        result = IndividualWorkerStats.fromJson(response.json())
        return result

    def get_individual_historical_worker_stats(self, address: str, worker: str) -> IndividualHistoricalWorkerStats:
        if address is None or worker is None:
            raise TypeError

        response = self._base_client.request(
            method='get',
            url=self.__individual_historical_worker_stats_path.format(address=address, worker=worker)
        )
        self._base_client.check_response(response, f'Failed to get All Worker Stats, {address}.')
        result = IndividualHistoricalWorkerStats.fromJson(response.json())
        return result

    def get_worker_monitoring(self, address: str, worker: str) -> IndividualHistoricalWorkerStats:
        if address is None or worker is None:
            raise TypeError

        response = self._base_client.request(
            method='get',
            url=self.__worker_monitoring_path.format(address=address, worker=worker)
        )
        self._base_client.check_response(response, f'Failed to get All Worker Stats, {address}.')
        result = IndividualHistoricalWorkerStats.fromJson(response.json())
        return result


    def _setPaths(self):
        # Base URL
        self.__base_path = self._url + '/miner'
        # Individual worker statistics
        # /miner/:miner/worker/:worker/currentStats
        self.__individual_worker_stats_path = self.__base_path + '/{address}/worker/{worker}/currentStats'
        # All worker statistics
        # /miner/:miner/workers
        self.__all_worker_stats_path = self.__base_path + '/{address}/workers'
        # Individual historical worker statistics
        # /miner/:miner/worker/:worker/history
        self.__individual_historical_worker_stats_path = self.__base_path + '/{address}/worker/{worker}/history'
        # Worker monitoring
        # /miner/:miner/worker/:worker/monitor
        self.__worker_monitoring_path = self.__base_path + '/{address}/worker/{worker}/monitor'
