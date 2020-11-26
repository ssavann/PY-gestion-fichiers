'''
Télécharger un fichier texte, image, pdf, etc...
'''

'''

#pour télécharger un fichier text

from urllib.request import urlopen

url = "https://www.learningcontainer.com/wp-content/uploads/2020/04/sample-text-file.txt"

with open("citation1.txt", "wb") as fic:
    temp = urlopen(url).read()
    fic.write(temp)


'''


#pour télécharger une image

from urllib.request import urlopen

url = "https://i.guim.co.uk/img/media/d69b5b434eab8de3bee564dd6041e30f7b8f6708/0_118_3500_2100/master/3500.jpg?width=620&quality=85&auto=format&fit=max&s=5548dd63a51944fb19d0c7f92e0e2020"

with open("image.jpg", "wb") as fic:
    temp = urlopen(url).read()
    fic.write(temp)
