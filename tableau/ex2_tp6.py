import numpy as np
mat=np.array([[1,2,3],[4,5,6]])
print(mat)
print(mat[1,2])
for i in range(3):
    somme_ligne=np.sum(mat[:,i])
    print("la somme de la colonne est : ",somme_ligne)



