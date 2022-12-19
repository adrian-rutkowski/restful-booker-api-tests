import pytest
from secrets import randbelow
from src.api.restful_booker_client import RestfulBookerClient
from src.config.config import AUTH_DATA
from src.utilities.utilities import generate_first_name
from src.utilities.utilities import generate_last_name
from src.utilities.utilities import generate_random_number
from src.utilities.utilities import generate_random_bool
from src.utilities.utilities import generate_booking_dates
from src.utilities.utilities import generate_random_string


@pytest.fixture(scope="session")
def auth_data():
    username = AUTH_DATA['username']
    password = AUTH_DATA['password']
    return username, password


@pytest.fixture(scope="session")
def authenticated_client(auth_data):
    client = RestfulBookerClient()
    response = client.create_token(auth_data[0], auth_data[1])
    token = response.response_body['token']
    auth_cookie = {"Cookie": "token=" + token, "Content-Type": "application/json"}
    client.session.headers.update(auth_cookie)
    return client


@pytest.fixture(scope="function")
def new_random_booking(authenticated_client):
    firstname = generate_first_name()
    lastname = generate_last_name()
    totalprice = generate_random_number()
    depositpaid = generate_random_bool()
    checkin = generate_booking_dates()[0]
    checkout = generate_booking_dates()[1]
    additionalneeds = generate_random_string()
    return authenticated_client.create_booking(firstname=firstname, lastname=lastname, totalprice=totalprice,
                                               depositpaid=depositpaid, checkin=checkin, checkout=checkout,
                                               additionalneeds=additionalneeds)


@pytest.fixture(scope="function")
def random_existing_booking_id(authenticated_client):
    response = authenticated_client.get_booking_ids()
    booking_id = response.response_body[randbelow(10)]['bookingid']
    return booking_id
