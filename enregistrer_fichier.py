'''
Gestion des fichiers en Python : Ouvrir un fichier
Mode d'ouverture:

				r 	Lecture
				w 	Ecriture (avec écrasement fichier)
				a 	Ajout
				x 	Lecture et Écriture
				r+	Lecture et Écriture (dans un même fichier)


Methodes:		read()
				readline()
				readlines()

'''

#fic = open("test.txt", "w")    #mode écriture, mais va effacer les précédentes
fic = open("test.txt", "a")     #mode ajout

fic.write("Ceci est une phrase.\n")
fic.write("Ceci est une seconde phrase.\n")

fic.close()


