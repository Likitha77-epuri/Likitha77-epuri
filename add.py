def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


m, n = input().split()
m, n = int(m), int(n)
num_list = []

for i in range(m):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)

# Write your code here
row_wise_max=[]
for row in num_list:
    row_wise_max.append(max(row))
maxi=max(row_wise_max)
row_index=row_wise_max.index(maxi)
max_row=num_list[row_index]
print(max_row)
column_index=max_row.index(maxi)
max_column=[]
for row in num_list:
    max_column.append(row[column_index])
print(max_column)
