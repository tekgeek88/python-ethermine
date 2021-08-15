import requests
from typing import Dict

"""
Access to the API is limited to 100 requests / 15 minutes / IP.
All information is cached for 2 minutes so there is no point in making more frequent requests.
Ethermine endpoint: https://api.ethermine.org
All endpoints are CORS enabled.
"""


class BaseClient(object):

    def __init__(self, url):
        self._url = url

    @property
    def url(self) -> str:
        return self._url

    def headers(self) -> Dict[str, str]:
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json'
        }
        return headers

    def request(self, method: str, url: str, params=None, data=None, headers=None, **kwargs):
        if not headers:
            headers = self.headers()
        return requests.request(method, url, params=params, data=data, headers=headers, **kwargs)

    def check_response(self, response, main_message: str):
        if response.status_code < 200 or response.status_code >= 300:
            status = response.status_code
            reason = response.text
            url = response.url
            error = f'{status}:{reason}.  URL {url}'
            response.close()
            message = main_message + '\n' + error
            raise Exception(message)
