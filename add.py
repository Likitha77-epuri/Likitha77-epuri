list_a=list(map(int,input().split()))
set_a=set(list_a)
max_num=max(set_a)
for i in range(1,max_num+2):
    if i not in set_a:
        print(i)
        break