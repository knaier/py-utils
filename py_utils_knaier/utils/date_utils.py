from datetime import date, datetime


def date_tomorrow() -> date:
    return datetime.date.today() + datetime.timedelta(days=1)


def date_today() -> date:
    return datetime.date.today()
