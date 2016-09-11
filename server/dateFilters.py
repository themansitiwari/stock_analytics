import datetime


def get_date_range_for_weeks(weeks):
    today = datetime.date.today()
    required_date = today - datetime.timedelta(days=weeks * 7)
    return [str(required_date), today]


def get_date_range_for_months(months):
    today = datetime.date.today()
    required_date = today - datetime.timedelta(days=months * 365 / 12)
    return [str(required_date), str(today)]


def get_date_range_for_years(years):
    today = datetime.date.today()
    required_date = today.replace(year=today.year - years)
    return [str(required_date), str(today)]
