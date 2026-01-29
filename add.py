def convert_string_to_int(num_list):
    new_list=[]
    for i  in num_list:
        num=int(i)
        new_list.append(num)
    return new_list
a=input().split(",")
b=input().split(",")
a=convert_string_to_int(a)
b=convert_string_to_int(b)
set_a=set(a)
set_b=set(b)
result=set_a.intersection(set_b)
result_list=list(result)
result_list.sort()
print(result_list)