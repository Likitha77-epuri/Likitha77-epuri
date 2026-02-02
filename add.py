e=input()
op_index=-1
for i in range(1,len(e)):
    if e[i] in "+-*/%":
        op_index=i 
        break
if op_index==-1:
    print("Invalid expression")
else:
        op=e[op_index]
        a=int(e[:op_index])
        b=int(e[op_index+1:])
        if op=="+":
            print(a+b)
        elif op=="-":
                print(a-b)
        elif op=="*":
            print(a*b)
        elif op=="/":
            if b!=0:
                print(a/b)
            else:
                print("Division by zero not allowed")
        elif op=="%":
            print(a%b)
        