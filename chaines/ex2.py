import random
def saisi(taille):
    mdp=""
    for i in range(taille):
        rand=random.randint(0,255)
        mdp=mdp+chr(rand)
    return mdp
taille=int(input("saisir la taille voulue: "))
while taille<4 :
    taille=int(input("erreur, saisir la taille voulue: "))
mdp=saisi(taille)
print(mdp)