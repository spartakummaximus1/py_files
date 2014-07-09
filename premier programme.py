annee = input("Saisissez une annee : ")
annee = int(annee)
bissectile = False
if annee % 400==0:
	bissectile= True
elif annee % 100 == 0:
	bissectile= False
elif annee % 4== 0:
	bissectile= True
else:
	bissectile= False

	
if bissectile:
	print("annee bissectile")
else:
	print("annee non bissectile")
os.system("pause")
	

	

