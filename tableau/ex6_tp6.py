import numpy as np
import random

def calcul_moy(notes):
    n,m=np.shape(notes)
    t=np.ndarray(n, dtype=float)
    for i in range(n):
        t[i]=np.mean(notes[i,:])
    return t

def meilleure_moy(t):
    return np.max(t)

def ajout(notes):
    n,m=np.shape(notes)
    mat=np.ndarray((n,m+1), dtype=int)
    for i in range(n):
        for j in range(m):
            mat[i,j]=notes[i,j]
        mat[i,m]=random.randint(0,20)
    return mat

# def ajout(notes):
#     n,m=np.shape(notes)
#     mat=[]
#     for i in range(n):
#         element=[]
#         for j in range(m):
#             element.append(notes[i,j])
#         element.append(random.randint(0,20))
#         mat.append(element)
#     return mat

notes = np.array([[12, 15, 14], [10, 11, 13], [18, 16, 17], [9, 8, 7], [14, 15, 16]])
t=calcul_moy(notes)
print("voici la moyenne de chaque etudiant\n")
print(t)
meilleure=meilleure_moy(t)
print("voici la meilleure moyenne \n")
print(meilleure)
m=ajout(notes)
print(m)
