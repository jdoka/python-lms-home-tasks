from datetime import datetime

moscow_times = datetime.strptime('Wednesday, October 2, 2002', "%A, %B %d, %Y")
guardian = datetime.strptime("Friday, 11.10.13", "%A, %d.%m.%y")
daily_news = datetime.strptime("Thursday, 18 August 1977", "%A, %d %B %Y")
print(moscow_times)
print(guardian)
print(daily_news)
