from ..base_client import BaseClient
from ..models.miner.dashboard import Dashboard
from ..models.miner.history import History
from ..models.miner.payouts import Payouts
from ..models.miner.rounds import Rounds
from ..models.miner.settings import Settings
from ..models.miner.statistic import Statistic


class Miner(object):
    def __init__(self, client: BaseClient):
        self._url = client.url
        self._base_client = client
        self._setPaths()

    def get_statistics(self, address: str) -> Statistic:

        if address is None:
            raise TypeError

        response = self._base_client.request(
            method='get',
            url=self.__statistic_path.format(address=address)
        )
        self._base_client.check_response(response, f'Failed to get Statistic, {address}.')
        result = Statistic.fromJson(response.json())
        return result

    def get_dashboard(self, address: str) -> Dashboard:

        if address is None:
            raise TypeError

        response = self._base_client.request(
            method='get',
            url=self.__dashboard_path.format(address=address)
        )
        self._base_client.check_response(response, f'Failed to get Dashboard, {address}.')
        result = Dashboard.fromJson(response.json())
        return result

    def get_history(self, address: str) -> History:

        if address is None:
            raise TypeError

        response = self._base_client.request(
            method='get',
            url=self.__history_path.format(address=address)
        )
        self._base_client.check_response(response, f'Failed to get Dashboard, {address}.')
        result = History.fromJson(response.json())
        return result

    def get_payouts(self, address: str) -> History:

        if address is None:
            raise TypeError

        response = self._base_client.request(
            method='get',
            url=self.__payouts_path.format(address=address)
        )
        self._base_client.check_response(response, f'Failed to get Dashboard, {address}.')
        result = Payouts.fromJson(response.json())
        return result

    def get_rounds(self, address: str) -> Rounds:

        if address is None:
            raise TypeError

        response = self._base_client.request(
            method='get',
            url=self.__rounds_path.format(address=address)
        )
        self._base_client.check_response(response, f'Failed to get Dashboard, {address}.')
        result = Rounds.fromJson(response.json())
        return result

    def get_settings(self, address: str) -> Settings:

        if address is None:
            raise TypeError

        response = self._base_client.request(
            method='get',
            url=self.__settings_path.format(address=address)
        )
        self._base_client.check_response(response, f'Failed to get Dashboard, {address}.')
        result = Settings.fromJson(response.json())
        return result

    def _setPaths(self):
        self.__base_path = self._url + '/miner'
        self.__dashboard_path = self.__base_path + '/{address}/dashboard'
        self.__history_path = self.__base_path + '/{address}/history'
        self.__payouts_path = self.__base_path + '/{address}/payouts'
        self.__rounds_path = self.__base_path + '/{address}/rounds'
        self.__settings_path = self.__base_path + '/{address}/settings'
        self.__statistic_path = self.__base_path + '/{address}/currentStats'
