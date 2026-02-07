m=int(input())
n=int(input())
found=False
for i in range(m,n+1):
    root=int(i**0.5)
    if root*root==i:
        print(i)
        found=True
        break
if not found:
    print("No Perfect Square")