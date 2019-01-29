# your code goes here
n=int(input())
sum1=0
p=n
while n!=0:
	t=n%10
	sum1=sum1*10+t
	n=n//10
if p==sum1:
	print("YES")
else:
	print("NO")
