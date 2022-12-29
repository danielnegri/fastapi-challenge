import decimal
from typing import Iterator, Tuple


def calculate_amortization_amount(
    principal: int, interest_rate: float, period: int
) -> float:
    """
    Calculates Amortization Amount per period.
    For more details: https://github.com/roniemartinez/amortization/blob/master/amortization/amount.py

    :param principal: Principal amount
    :param interest_rate: Interest rate per period
    :param period: Total number of period
    :return: Amortization amount per period
    """
    adjusted_interest = interest_rate / 12
    x = (1 + adjusted_interest) ** period
    return round(principal * (adjusted_interest * x) / (x - 1), 2)


def amortization_schedule(
    principal: int, annual_interest_rate: decimal, period: int
) -> Iterator[Tuple[int, float, float, float, float]]:
    """
    Generates amortization schedule.
    For more details: https://github.com/roniemartinez/amortization/blob/master/amortization/schedule.py

    :param principal: Principal amount
    :param annual_interest_rate: Interest rate per period
    :param period: Total number of periods
    :return: Rows containing period, amount, interest, principal, balance, etc
    """
    amortization_amount = calculate_amortization_amount(
        principal, annual_interest_rate, period
    )
    adjusted_interest = annual_interest_rate / 12
    balance = principal
    for number in range(1, period + 1):
        interest = round(balance * adjusted_interest, 2)
        if number < period:
            principal = amortization_amount - interest
            balance -= principal
        else:
            principal, amortization_amount, balance = balance, balance + interest, 0
        yield number, amortization_amount, interest, principal, balance
