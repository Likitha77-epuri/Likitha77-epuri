def get_sum_list(int_list):
    con_sum_list=[]
    end_index=len(int_list)-1
    for i in range(end_index):
        sum_list=int_list[i]+int_list[i+1]
        con_sum_list.append(sum_list)
    return con_sum_list
def print_triangle(int_list):
    while len(int_list)>1:
        con_sum_list=get_sum_list(int_list)
        print(con_sum_list)
        int_list=con_sum_list
def convert_string_to_int(str_num_list):
    new_list=[]
    for i in str_num_list:
        num=int(i)
        new_list.append(num)
    return new_list
str_num_list=input().split(",")
int_list=convert_string_to_int(str_num_list)
print(int_list)
print_triangle(int_list)