l=[2,3,2,4,56,6]
def greatest(l):
	a=0
	for e in l:
		if a<e:
			a=e
	return a
print(greatest(l))