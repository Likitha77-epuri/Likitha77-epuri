from datetime import datetime,timedelta
data=input()
n=int(input())
data_obj=datetime.strptime(data,"%b %d %Y")
d_2=data_obj+timedelta(days=n*365)
print(d_2)