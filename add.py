list_a=input().split(",")
num_list=[]
for i in list_a:
    is_digit=i.isdigit()
    if is_digit:
        num=int(i)
        num_list.append(num)
print(num_list)