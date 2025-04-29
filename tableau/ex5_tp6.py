import numpy as np
mat=np.random.rand(3, 3)
print(mat)

for i in range(3):
    print("la somme de chaque ligne est :",np.sum(mat[i,:]))

for i in range(3):
    for j in range(3):
        if mat[i][j]>0.5:
            mat[i][j]=1
print(mat)
