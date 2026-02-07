s1=input().strip()
s2=input().strip()
if len(s1)!=len(s2):
    print("No Match")
else:
    count=-1
    temp=s1
    for i in range(len(s1)):
        if temp==s2:
            count=i
            break
        temp=temp[-1]+temp[:-1]
    if count==-1:
        print("No Match")
    else:
        print(count)