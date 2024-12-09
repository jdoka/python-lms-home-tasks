from datetime import datetime
from datetime import timedelta


def date_range(start_date, end_date):
    result = []
    try:
        date_format = "%Y-%m-%d"
        start_date_as_date = datetime.strptime(start_date, date_format)
        end_date_as_date = datetime.strptime(end_date, date_format)
        date = start_date_as_date
        while date <= end_date_as_date:
            result.append(date.strftime(date_format))
            date = date + timedelta(days=1)
    finally:
        return result


print(date_range("2022-05-01", "2022-05-03"))  # ['2022-05-01', '2022-05-02', '2022-05-03']
print(date_range("2022-05-07", "2022-05-03"))  # []
print(date_range("2022.05.01", "2022-05-03"))  # []
print(date_range("", ""))  # []
