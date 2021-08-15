import json

from typing import Dict


class Dashboard(object):

    def __init__(self, statistics=None, workers=None, current_statistics=None, settings=None):
        self._statistics = statistics
        self._workers = workers
        self._current_statistics = current_statistics
        self._settings = settings

    @property
    def statistics(self) -> list:
        return self._statistics

    @statistics.setter
    def statistics(self, value: list):
        self._statistics = value

    @property
    def workers(self) -> list:
        return self._workers

    @workers.setter
    def workers(self, value: list):
        self._workers = value

    @property
    def current_statistics(self) -> list:
        return self._current_statistics

    @current_statistics.setter
    def current_statistics(self, value: list):
        self._current_statistics = value

    @property
    def settings(self) -> dict:
        return self._settings

    @settings.setter
    def settings(self, value: dict):
        self._settings = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        result = {}
        result["statistics"] = self.statistics
        result["workers"] = self.workers
        result["current_statistics"] = self.current_statistics
        result["settings"] = self.settings
        return result

    @staticmethod
    def fromJson(content: Dict):
        result = Dashboard()
        data = content.get("data", {})

        if 'statistics' in data:
            statistics = data['statistics']
            if statistics is not None and len(statistics) > 0:
                result.statistics = []
                for value in statistics:
                    result.statistics.append(value)

        if 'workers' in data:
            workers = data['workers']
            if workers is not None and len(workers) > 0:
                result.workers = []
                for value in workers:
                    result.workers.append(value)

        if 'currentStatistics' in data:
            current_statistics = data['currentStatistics']
            if current_statistics is not None and len(current_statistics) > 0:
                result.current_statistics = {}
                for key, value in current_statistics.items():
                    result.current_statistics[key] = value

        if 'settings' in data:
            settings = data['settings']
            if settings is not None and len(settings) > 0:
                result.settings = {}
                for key, value in settings.items():
                    result.settings[key] = value

        return result
