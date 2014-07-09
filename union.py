a=[1,3,4,2,4,5,4]
b=[3,5,3,5,6,4,3]

def union(a,b):
	return a+b or b+a

print(union(a,b))