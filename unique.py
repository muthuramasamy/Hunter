# your code goes here
n=int(input())
l=list(map(int,input().split()))
l2=[]
c=0
s=set([i for i in l if l.count(i)==1 ])
for i in s:
	l2.append(i)
	c=1
l2.sort
if c==1:
	for i in range(len(l2)):
		if i==len(l2)-1:
			print(l2[i],end='')
		else:
			print(l2[i],end=' ')
else:
	print('unique')
