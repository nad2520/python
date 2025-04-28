liste= ["Ordinateur", "Clavier",
"Clavier", "Souris", "Clavier"]
test=False
for element in liste:
    if element=="Routeur":
        test=True
if test==False:
    print("n'est pas disponible")
else:
    print("est disponible")
