from datetime import datetime


def nth_day_of_next_month(dt: datetime, day: int = 1) -> datetime:
    """Get the first day of the next month. Preserves the timezone.

    Args:
        dt (datetime.datetime): The current datetime
        day (int): N-th day of the month

    Returns:
        datetime.datetime: The n-th day of the next month at 00:00:00.
    """
    if dt.month == 12:
        return datetime(year=dt.year + 1, month=1, day=day, tzinfo=dt.tzinfo)
    else:
        return datetime(year=dt.year, month=dt.month + 1, day=day, tzinfo=dt.tzinfo)
