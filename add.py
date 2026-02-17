from datetime import datetime,timedelta
d1=input()
d2=input()
d1_obj=datetime.strptime(d1,"%d %b %Y")
d2_obj=datetime.strptime(d2,"%d %b %Y")
one_day=timedelta(days=1)
sat=0
sun=0
while d1_obj<=d2_obj:
    if d1_obj.strftime("%A")=="Saturday":
        sat+=1 
    elif d1_obj.strftime("%A")=="Sunday":
        sun+=1 
    d1_obj+=one_day
print("Saturday:" , sat)
print("Sunday:" , sun)
    
