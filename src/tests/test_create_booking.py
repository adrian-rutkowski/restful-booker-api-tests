import pytest
import allure
from assertpy import assert_that


@allure.title("POST /booking/:id - empty payload")
def test_empty_payload(authenticated_client):
    payload = {}
    response = authenticated_client.create_booking(payload=payload)

    assert_that(response.status_code).is_equal_to(500)
    assert_that(response.response_body).is_equal_to("Internal Server Error")


@allure.title("POST /booking/:id - total price input format - [{total_price}]")
@pytest.mark.parametrize("total_price, expected_status_code",
                         [("100", 200), ("-200", 400), ("300,00", 200), ("400.00", 200), (500, 200), ("string", 400),
                          ("", 400), (None, 500)])
def test_payload_price_validation(authenticated_client, total_price, expected_status_code):
    response = authenticated_client.create_booking(totalprice=total_price)

    assert_that(response.status_code).is_equal_to(expected_status_code)
