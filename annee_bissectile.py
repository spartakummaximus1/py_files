#-*-coding:Latin-1 -*

 import os
 
 
 annee=input("Saisissez l'annee que vouz voulez:")

 annee=int(annee)
 if annee%400==0 or (annee%4==0 and annee%100!=0):
	print("L'annee sasie est bissectile")
else:
	print("L'annee saisie n'est pas bissectile")

	


 os.system("pause")


