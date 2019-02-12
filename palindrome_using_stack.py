#hy guvi
class stack:
	def __init__(self):
		self.items=[]
	def is_empty(self):
		return self.items==[]
	def push(self,data):
		self.items.append(data)
	def pop(self):
		return self.items.pop()
s=stack()
n=input()
for i in n:
	s.push(i)
r=''
while not s.is_empty():
	r = r + s.pop()
	
if n==r:
	print("YES")
else:
	print('NO')
	
