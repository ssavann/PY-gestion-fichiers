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

with open("note.txt", "r") as fic:
    data=fic.read()

print(data)



if fic.closed: print("fichier fermé.")



