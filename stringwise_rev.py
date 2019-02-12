#your code goes here
n=list(map(str,input().split()))
for i in range(len(n)):
	n[i]=n[i][::-1]
for i in range(len(n)):
	if i==len(n)-1:
		print(n[i],end="")
	else:
		print(n[i],end=" ")
