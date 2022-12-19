import pytest
import allure
from assertpy import assert_that
from assertpy import soft_assertions
from src.utilities.schema_validator import validate_schema
from src.utilities.schemas import GET_BOOKING_SCHEMA


@allure.title("GET /booking")
@pytest.mark.regression
def test_get_booking_ids(authenticated_client):
    response = authenticated_client.get_booking_ids()

    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.response_body).is_not_empty()


@allure.title("GET /booking/:id")
@pytest.mark.regression
def test_get_booking(authenticated_client, random_existing_booking_id):
    booking_id = random_existing_booking_id
    response = authenticated_client.get_booking(booking_id)
    validation = validate_schema(GET_BOOKING_SCHEMA, response.response_body)

    assert_that(response.status_code).is_equal_to(200)
    with soft_assertions():
        assert_that(response.response_body).is_not_empty()
        assert_that(validation).is_true()


@allure.title("POST /booking")
@pytest.mark.regression
def test_create_booking(authenticated_client):
    response = authenticated_client.create_booking()

    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.response_body).is_not_empty()
    assert_that(response.response_body).contains_key('bookingid')


@allure.title("PUT /booking/:id")
@pytest.mark.regression
def test_update_booking(authenticated_client, random_existing_booking_id):
    response = authenticated_client.update_booking(random_existing_booking_id)

    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.response_body).is_not_empty()
    assert_that(response.response_body).contains_key('firstname')


@allure.title("PATCH /booking/:id")
@pytest.mark.regression
def test_partial_update_booking(authenticated_client, random_existing_booking_id):
    response = authenticated_client.partial_update_booking(random_existing_booking_id)

    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.response_body).is_not_empty()
    assert_that(response.response_body).contains_key('firstname')


@allure.title("DELETE /booking/:id")
@pytest.mark.regression
def test_delete_booking(authenticated_client, new_random_booking):
    booking_id = new_random_booking.response_body["bookingid"]
    response = authenticated_client.delete_booking(booking_id)

    assert_that(response.status_code).is_equal_to(201)
    assert_that(response.response_body).is_not_empty()
