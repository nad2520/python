produits = ["Ordinateur", "Clavier", "Souris", "Écran",
"Imprimante"]
quantites = [15, 30, 50, 10, 5]
i=0
for element in produits:
    print(element," : ",quantites[i]," unités")
    i=i+1
liste=[]
i=0
for element in quantites:
    liste.append((element)-5)
print(liste)
