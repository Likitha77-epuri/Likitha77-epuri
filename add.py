import datetime
zero=datetime.datetime(1970,1,1)
u=int(input())
seconds=datetime.timedelta(seconds=u)
result=zero+seconds
dt_format="%Y-%m-%d %H:%M:%S"
print(result.strftime(dt_format))