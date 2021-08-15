from ..base_client import BaseClient
from ..models.pool.basic_pool_stats import BasicPoolStats
from ..models.pool.mined_blocks_stats import MinedBlocksStats
from ..models.pool.network_statistics import NetworkStatistics
from ..models.pool.server_hashrate_stats import ServerHashrateStats


class Pool(object):
    def __init__(self, client: BaseClient):
        self._url = client.url
        self._base_client = client
        self._setPaths()

    def get_basic_pool_stats(self) -> BasicPoolStats:
        response = self._base_client.request(
            method='get',
            url=self.__basic_pool_stats_path
        )
        self._base_client.check_response(response, f'Failed to get Basic Pool Stats.')
        result = BasicPoolStats.fromJson(response.json())
        return result

    def get_mined_blocks_stats(self) -> MinedBlocksStats:
        response = self._base_client.request(
            method='get',
            url=self.__mined_block_stats_path
        )
        self._base_client.check_response(response, f'Failed to get Basic Pool Stats.')
        result = MinedBlocksStats.fromJson(response.json())
        return result

    def get_network_statistics(self) -> NetworkStatistics:
        response = self._base_client.request(
            method='get',
            url=self.__network_stats_path
        )
        self._base_client.check_response(response, f'Failed to get Basic Pool Stats.')
        result = NetworkStatistics.fromJson(response.json())
        return result

    def get_server_hashrate_stats(self) -> ServerHashrateStats:
        response = self._base_client.request(
            method='get',
            url=self.__server_hashrate_stats_path
        )
        self._base_client.check_response(response, f'Failed to get Basic Pool Stats.')
        result = ServerHashrateStats.fromJson(response.json())
        return result

    def _setPaths(self):
        # Base URL
        self.__base_path = self._url
        # Basic Pool Stats
        # /poolStats
        self.__basic_pool_stats_path = self.__base_path + '/poolStats'
        # Mined Blocks Stats
        # /blocks/history
        self.__mined_block_stats_path = self.__base_path + '/blocks/history'
        # Network Statistics
        # /networkStats
        self.__network_stats_path = self.__base_path + '/networkStats'
        # Server Hashrate Stats
        # /servers/history
        self.__server_hashrate_stats_path = self.__base_path + '/servers/history'
