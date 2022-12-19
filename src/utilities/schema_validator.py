from cerberus import Validator
from src.utilities.logger import get_logger


def validate_schema(schema, response):
    log = get_logger()
    v = Validator(schema)
    # Optional
    # v.allow_unknown = True
    if v.validate(response):
        return True
    else:
        log.error(v.errors)
        return False
