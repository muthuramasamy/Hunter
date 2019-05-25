# your code goes here
n=int(input())
li=list(map(int,input().split()))
a=[]
b=[]
flag=0
for i in li:
	d=n*i
	if d in li:
		a.append(i)
		for i in a:
			print(i)
			flag=1
	else:
		b.append(d)
if flag==0:
	for i in b:
		c=i*0
	print (c)
	
