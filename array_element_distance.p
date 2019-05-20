# your code goes here
n=int(input())
arr=list(map(int,input().split()))
u,v=map(int,input().split())
c=0
d=0
e=0
f=0
for i in range (0,len(arr)):
	if arr[i]==u:
		c=c+1
		if c==1:
			e=e+i
	elif arr[i]==v:
		d+=1
		if d==1:
			f=f+i
print(abs(f-e))
	
