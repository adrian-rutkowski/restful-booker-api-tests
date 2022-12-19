import pytest
import allure
from assertpy import assert_that


@allure.title("GET /booking - filtering - [{filter_key}: {filter_value}]")
@pytest.mark.parametrize("filter_key, filter_value", [("firstname", "Jack"),
                                                      ("lastname", "Mount")])
def test_get_bookings_filters(authenticated_client, filter_key, filter_value):
    response = authenticated_client.get_booking_ids({filter_key: filter_value})

    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.response_body).is_not_empty()
