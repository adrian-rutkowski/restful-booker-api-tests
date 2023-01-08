# restful-booker-api-tests
![example workflow](https://github.com/adrian-rutkowski/restful-booker-api-tests/actions/workflows/job.yml/badge.svg)

Sample api test automation framework based on https://restful-booker.herokuapp.com/

Features:
- authentication data kept in the config file
- random utilities to create the payload data
- endpoint paths extracted to a single file
- test parametrization utilizing pytest.parametrize marker
- pytest markers
- soft assertions
- allure reports and dynamic titles
- debug logging
- cerberus schema validation
- triggers github actions on push to main
- flake8 linting check
- dockerfile to create an image that will run the regression tests in CI/CD

To run the tests locally and generate a report:

`pytest -v -s -m regression --alluredir="src/tests/reports/allure_raw"`

`allure serve "src/tests/reports/allure_raw"`
