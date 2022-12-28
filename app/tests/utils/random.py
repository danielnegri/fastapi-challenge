import random
import string
from decimal import Decimal


def random_decimal(low: int = 0, high: int = 10) -> Decimal:
    return Decimal(round(random.randint(low, high), 5))


def random_lower_string(size: int = 8) -> str:
    return "".join(random.choices(string.ascii_lowercase, k=size))


def random_email() -> str:
    return f"{random_lower_string()}@{random_lower_string()}.com"
