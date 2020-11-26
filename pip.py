'''
PIP  -> Système de gestion de paquets

pip install translate
'''
from translate import Translator 

txt = input("text a traduire ? ")

translator = Translator(to_lang="fr")

print("Traduction en cours...")
traduction = translator.translate(txt)

print(traduction)