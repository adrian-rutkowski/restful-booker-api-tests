from src.config.config import BASE_URI
from dataclasses import dataclass
import requests
from src.utilities.logger import get_logger


@dataclass
class Response:
    status_code: int
    response_body: object
    headers: dict


class APIClient:
    def __init__(self):
        self.base_url = BASE_URI
        self.session = requests.Session()

    log = get_logger()

    def get(self, endpoint):
        url = self.base_url + endpoint
        self.log.debug(f'Sending GET request to {url}')
        response = self.session.get(url)
        return self.__get_responses(response)

    def post(self, endpoint, payload=None):
        url = self.base_url + endpoint
        self.log.debug(f'Sending POST request to {url} with payload: {payload}')
        response = self.session.post(url=url, data=payload)
        return self.__get_responses(response)

    def put(self, endpoint, payload=None):
        url = self.base_url + endpoint
        self.log.debug(f'Sending PUT request to {url} with payload: {payload}')
        response = self.session.put(url=url, data=payload)
        return self.__get_responses(response)

    def patch(self, endpoint, payload=None):
        url = self.base_url + endpoint
        self.log.debug(f'Sending PATCH request to {url} with payload: {payload}')
        response = self.session.patch(url=url, data=payload)
        return self.__get_responses(response)

    def delete(self, endpoint):
        url = self.base_url + endpoint
        self.log.debug(f'Sending DELETE request to {url}')
        response = self.session.delete(url)
        return self.__get_responses(response)

    def __get_responses(self, response):
        status_code = response.status_code

        try:
            body = response.json()
        except Exception:
            body = response.text

        headers = response.headers

        return Response(
            status_code, body, headers
        )
