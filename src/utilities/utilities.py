import names
import random
import datetime
import string


def generate_first_name():
    return names.get_first_name()


def generate_last_name():
    return names.get_last_name()


def generate_random_number(low=1, high=10000):
    return random.randint(low, high)


def generate_random_bool():
    return bool(random.getrandbits(1))


def generate_booking_dates(number_of_days=7):
    check_in = datetime.date.today()
    check_out = check_in + datetime.timedelta(days=number_of_days)
    return check_in.strftime("%Y-%m-%d"), check_out.strftime("%Y-%m-%d")


def generate_random_string(length=15):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))
