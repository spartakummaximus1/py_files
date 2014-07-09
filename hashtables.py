import os

l='lilavois\n manmi\n brun\n manit\n john\n obed\n'
print('voici votre liste de contacts:\n',l)
person=input('tapez le nom de votre contact et le numero apparaitra immediatement: ')
def number_phone_of(person):
	contacts={'lilavois':44139593,'manmi':37695954,'brun':31159103,'manit':11223322,'john':20399321,'obed':45399373}
	for name in contacts:
		if person in contacts:
			return contacts[person]
		else:
			print("ce nom n'appartient pas a vos contacts.")
			break
print(number_phone_of(person))

while 1:
	cont= input('tapez "n" pour continuer ou "q" pour quitter :')
	if cont== "n":
		person=input("entrez le nom d'un contact: ")
		def number_phone_of(person):
			contacts={'lilavois':44139593,'manmi':37695954,'brun':31159103}
			for name in contacts:
				if person in contacts:
					return contacts[person]
				else:
					return print("ce nom n'appartient pas a vos contacts.")
					break
		print(number_phone_of(person))
	elif cont== "q":
		break
	else:
		pass
