liste=["Ordinateur", "Clavier", "Souris", "Écran", "Imprimante",
"Disque Dur", "Webcam", "Routeur", "Casque",
"Microphone"]
print("voici l'affichage de la liste entière")
print(liste)
print("voici l'affichage de premier produit")
print(liste[0])

liste.append("Scanner")
liste.remove("Microphone")
print(liste)

for element in liste:
    print("Produit en stock: ",element)
print("\n")
i=0
for element in liste:
    i=i+1
print("Il y a ",i," produits en stock" )

print("la liste triée est")
liste.sort()
print(liste)

pos=liste.index("Écran")
liste.remove("Écran")
liste.insert(pos,"Moniteur 4K")
print(liste)
