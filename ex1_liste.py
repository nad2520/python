liste =[] #création d'une liste
ch1="abc"
ch2="de"
ch=""
for i in range(len(ch1)):
    for j in range(len(ch2)):
        ch=ch1[i]+ch2[j]
        liste.append(ch)
print(liste)