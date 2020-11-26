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

fic = open("note.txt", "r")

data= fic.read()
#data= fic.readline()
#data= fic.readlines()

print(data)





fic.close()