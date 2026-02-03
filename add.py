s=input()
total=0
count=0
for ch in s:
    if ch.isdigit():
        total+=int(ch)
        count+=1 
if count>0:
    avg=round(total/count,2)
    print(total)
    print(avg)
else:
    print(0)
    print(0)