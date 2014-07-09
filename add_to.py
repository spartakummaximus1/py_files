index=[]
keyword=input('Saisissez le keyword: ')
def add_to_index(index,keyword,url):
	for el in index:
		if el[0]==keyword:
			el[1].append(url)
	index.append([keyword,[url]])
	
add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'udacity','http://npr.org')
add_to_index(index,'computing','http://acm.com')

def lookup(index,keyword):
	for el in index:
		if el[0]==keyword:
			print(el[1])
print(lookup(index,keyword))

		