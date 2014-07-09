l=[2,4,2,5]
m=4
def find_element(l,m):
	if m in l:
		r=(l.index(m))
		return r
	else:
		print(-1)

print(find_element(l,m))	