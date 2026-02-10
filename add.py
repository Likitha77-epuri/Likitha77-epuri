def string_to_int(list_a):
    new_list=[]
    for i in list_a:
        num=int(i)
        new_list.append(num)
    return new_list
num_list=input().split()
num_list=string_to_int(num_list)
ma=max(num_list)
num_set=set(num_list)
first=set(range(1,ma+1))
missing=first.difference(num_set)
missing=list(missing)
missing.sort()
print(missing)