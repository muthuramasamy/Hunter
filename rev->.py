# your code goes here
n=int(input())
li=list(map(int,input().split()))
for i in range(n-1,-1,-1):
	if i==0:
		print(li[i],end="")
	else:
		print(li[i],end="->")
	
