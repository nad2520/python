import numpy as np

def saisi():
    n=int(input("n= "))
    while not(0<n<=10):
        n=int(input("n= "))
    return n

def remplirNotes(n,m):
    notes=np.ndarray((n,m), dtype=int)
    for i in range (n):
        for j in range (m):
            notes[i,j]=int(input("votre note est: "))
    return notes

def calculMoyElev(notes):
    n,m=np.shape(notes)
    t=[]
    for i in range (n):
        element=np.mean(notes[i,:])
        t.append(element)
    return np.array(t)

def calculMoy(t):
    return np.mean(t)
        

n=saisi()
m=saisi()
notes=remplirNotes(n,m)
print("voici les notes des eleves \n")
print(notes)
t=calculMoyElev(notes)
print("voici les moyennes des eleves \n")
print(t)
moy=calculMoy(t)
print("voici la moyenne de la classe \n")
print(moy)
