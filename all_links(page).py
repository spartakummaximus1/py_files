import os
page='<a href="facebook.com"><a href="google.com"><a href="udacity.com"><a href="yahoo.com">'
def get_next_target(page):
	start_link=page.find('href=')
	start_quote=page.find('"',start_link)
	end_quote=page.find('"',start_quote+1)
	url=page[start_quote+1:end_quote]
	return url,end_quote
	
def all_links(page):
	link=[]
	while(True):
		url,endpos= get_next_target(page)
		if url:
			link.append(url)
			page=page[endpos:]
		else:
			break
	return link
	
input=input('Saisissez votre lien url: ')
def search(input,page):
	links=all_links(page)
	for e in links:
		if input in e:
			return e
		
print(search(input,page))
os.system('pause')
 
