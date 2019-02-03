# your code goes here
n,k=map(int,input().split())
l=list(map(int,input().split()))
l1=list(map(int,input().split()))
f=0
for i in l1:
    if i in l:
        f=f+1
    
if f==len(l1):
    print("YES")
    
else:
    print("NO")
