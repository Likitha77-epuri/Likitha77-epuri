from datetime import datetime,timedelta
start=input()
end=input()
start_dt=datetime.strptime(start,"%b %d %Y")
end_dt=datetime.strptime(end,"%b %d %Y")
n=(end_dt-start_dt).days
for i in range(n+1):
    current=start_dt+timedelta(days=i)
    print(current)