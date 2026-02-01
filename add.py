def convert_to_string(str_list):
    int_list=[]
    for str_num in str_list:
        num=int(str_num)
        int_list.append(num)
    return int_list
def convert_to_list(keys_list,value_list):
    dict_a={}
    n_keys=len(keys_list)
    for i in range(n_keys):
        key=keys_list[i]
        value=value_list[i]
        dict_a[key]=value 
    return dict_a
dict_a_keys=input().split()
dict_a_values=input().split()
dict_b_keys=input().split()
dict_b_values=input().split()
dict_a_values=convert_to_string(dict_a_values)
dict_b_values=convert_to_string(dict_b_values)
student_details1=convert_to_list(dict_a_keys,dict_a_values)
student_details2=convert_to_list(dict_b_keys,dict_b_values)
student_details1.update(student_details2)
student_details=student_details1.items()
student_details=sorted(student_details)
print(student_details)