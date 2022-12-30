import calendar
from datetime import datetime

from dateutil import relativedelta


def nth_day_of_next_month(dt: datetime, day: int) -> datetime:
    """Get the first day of the next month. Preserves the timezone.

    Args:
        dt (datetime.datetime): The current datetime
        day (int): N-th day of the month

    Returns:
        datetime.datetime: The n-th day of the next month at 00:00:00.
    """
    next_month = dt + relativedelta.relativedelta(months=1)
    next_day = min(
        calendar.monthrange(year=next_month.year, month=next_month.month)[1], day
    )
    return next_month.replace(day=next_day)
