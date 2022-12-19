from src.api.api_client import APIClient
from src.config import endpoints
import json
import urllib.parse


class RestfulBookerClient(APIClient):

    def create_token(self, username, password, payload=None):
        if payload is None:
            payload = {
                "username": username,
                "password": password
            }

        return self.post(endpoint=endpoints.auth, payload=payload)

    def get_booking_ids(self, expected_filter: dict = None):

        if expected_filter is not None:
            formatted_filter = urllib.parse.urlencode(expected_filter)
            return self.get(endpoint=endpoints.booking + f"?{formatted_filter}")
        else:
            return self.get(endpoint=endpoints.booking)

    def get_booking(self, booking_id):
        return self.get(endpoint=f'{endpoints.booking}/{booking_id}')

    def delete_booking(self, booking_id):
        return self.delete(endpoint=f'{endpoints.booking}/{booking_id}')

    def create_booking(self,
                       payload=None,
                       firstname="Jack",
                       lastname="Grealish",
                       totalprice=10000,
                       depositpaid=True,
                       checkin="2018-01-01",
                       checkout="2019-01-01",
                       additionalneeds="Breakfast"):
        if payload is None:
            payload = {
                "firstname": firstname,
                "lastname": lastname,
                "totalprice": totalprice,
                "depositpaid": depositpaid,
                "bookingdates": {
                    "checkin": checkin,
                    "checkout": checkout
                },
                "additionalneeds": additionalneeds
            }

        return self.post(endpoint=endpoints.booking, payload=json.dumps(payload))

    def update_booking(self,
                       booking_id: int = "",
                       payload=None,
                       firstname="Jack",
                       lastname="Grealish",
                       totalprice=10000,
                       depositpaid=True,
                       checkin="2018-01-01",
                       checkout="2019-01-01",
                       additionalneeds="Breakfast"):
        if payload is None:
            payload = {
                "firstname": firstname,
                "lastname": lastname,
                "totalprice": totalprice,
                "depositpaid": depositpaid,
                "bookingdates": {
                    "checkin": checkin,
                    "checkout": checkout
                },
                "additionalneeds": additionalneeds
            }

        return self.put(endpoint=f'{endpoints.booking}/{booking_id}', payload=json.dumps(payload))

    def partial_update_booking(self,
                               booking_id="",
                               payload=None,
                               firstname="Mason",
                               lastname="Mount"):
        if payload is None:
            payload = {
                "firstname": firstname,
                "lastname": lastname
            }
        return self.patch(endpoint=f'{endpoints.booking}/{booking_id}', payload=json.dumps(payload))
