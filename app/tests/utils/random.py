import random
import string


def random_lower_string(size: int = 8) -> str:
    return "".join(random.choices(string.ascii_lowercase, k=size))


def random_email() -> str:
    return f"{random_lower_string()}@{random_lower_string()}.com"
