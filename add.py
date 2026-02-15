from datetime import datetime,timedelta
date=input()
date_format="%d %b %Y"
today=datetime.strptime(date,date_format)
yes=today-timedelta(days=1)
day=today+timedelta(days=1)
print(yes)
print(today)
print(day)