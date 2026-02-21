from datetime import datetime
y_a,y_b=input().split()
mon=0
months=range(1,13)
for y in range(int(y_a),int(y_b)+1):
    for m in months:
        datetime_obj=datetime(y,m,1)
        name=datetime_obj.strftime("%A")
        if name=="Monday":
            mon+=1 
print(mon)