from datetime import datetime
date=input()
date_format="%b %d %Y %I:%M %p"
dt_obj=datetime.strptime(date,date_format)
new=datetime(dt_obj.year+1,1,1)
dt_diff=new-dt_obj
h=dt_diff.days*24+dt_diff.seconds//3600
m=(dt_diff.seconds//60)%60
print("{} hours {} minutes".format(h,m))